require 'nokogiri'
require 'open-uri' 
require 'csv'
require 'fileutils'


module Scraper

	class FoodEstabs

		attr_accessor :search_url, :estab_url, :search_page_count, :counter, :start_number, :page, :estab_id,
									:inspection_key, :today


		def initialize
			@search_url = 'http://samhd.tx.gegov.com/San%20Antonio/search.cfm?start='
			@estab_url = 'http://samhd.tx.gegov.com/San%20Antonio/'
			@search_page_count = 794
			@counter = 1
			@start_number = 1
			@today = Time.new.strftime("%m_%d_%y")
		end

		def fetch
			path = "estab_inspecs/raw/#{@today}/search_pages"
			FileUtils.mkdir_p(path) unless File.exists?(path)

			until @counter > @search_page_count 

				puts "On search page: #{@counter}."	

				url = "#{@search_url}#{@start_number}"
				@page = open(url).read 
				write_to_search_dir(@page)
				@counter += 1
				@start_number += 10
				@page  = ""
				sleep 1
			end
		end

		def get_estab_pages	
			path = "estab_inspecs/raw/#{@today}/estabs"
			FileUtils.mkdir_p(path) unless File.exists?(path)

			filenames = Dir["estab_inspecs/raw/#{@today}/search_pages/*.html"]
			estabs_dir = Dir['estab_inspecs/raw/#{@today}/estabs/']


			filenames.each do |file|

				 puts "On file: #{file}"
				 html = Nokogiri::HTML(File.open(file, 'r'))
				 links = html.css('table td a').map { |link| link['href'] }
				
				links.each do |link|
				 	if link =~ /estab.cfm\?licenseID=/

				 		if File.exists?(File.join(estabs_dir, "#{link}.html"))
				 			puts "File #{link}.html exists."
				 		else
				 			@estab = open("#{@estab_url}#{link}").read
				 			write_to_estabs_dir( link, @estab )
				 			@estab = ''
				 			sleep 1
				 			
				 		end
				 	end
				end

			end
		end

		def process_estabs
			path = "estab_inspecs/processed/#{today}"
			FileUtils.mkdir_p(path) unless File.exists?(path)


			filenames = Dir["estab_inspecs/raw/#{today}/estabs/*.html"]


			filenames.each do |file|
				estabs = []
				@estab_id = file.match(/(?<=licenseID=)\d+/).to_s
			
				estabs << estab_id

				html = Nokogiri::HTML(File.open(file,'r'))

					name = html.css("#demographic b[style='font-size:14px;']").text
					estabs << name

					init_addy = html.css("#demographic i").text.gsub(/\t|\r|\n|« Back/, '').split(' ')
					clean_addy = init_addy.join(' ').gsub(/\s(?=,)/, '')

					estabs << clean_addy

					write_to_csv(estabs, 'estabs_tbl')
					
					inspections = html.css("div[style='border:1px solid #003399;width:95%;margin-bottom:10px;']").collect

					inspections.each do |inspection|
						inspects = []

						dd_bits = inspection.css("div[style='padding:5px;']").text.gsub(/\t|\r|\n/, '')
						
						date = dd_bits.match(/\d\d\/\d\d\/\d\d\d\d/).to_s
						@inspection_key = "#{estab_id}-#{date}"

						demerits = dd_bits.match(/Demerits\s\d+/).to_s
						demerits_nums = demerits.match(/\d+/).to_s
						
						inspects << estab_id
						inspects << date
						inspects << demerits
						inspects << demerits_nums
						inspects << inspection_key


						write_to_csv(inspects, 'inspections_tbl')

						descs = inspection.css("div[style='background-color:#EFEFEF;padding:5px;']").collect

						
						descs.each do |desc|
							descs_arr =[]
							desc_text = desc.text.chomp.strip.gsub(/"|'|\n|\r/, '')
							desc_text == '' ? viol_text = 'No Descriptions' : viol_text = desc_text
							descs_arr << @estab_id
							descs_arr << @inspection_key
							descs_arr << viol_text

							write_to_csv(descs_arr, 'descs_tbl')
						end

					end		
				
			end
		end


		private 
		def write_to_csv(data=[], file)
			CSV.open("estab_inspecs/processed/#{today}/#{file}.csv", "a") do |csv|
				csv << data
			end
		end

		def write_to_search_dir(page)
			fh = File.open("estab_inspecs/raw/#{@today}/search_pages/#{@start_number}.html", "w" )
        		fh.write(page)
        	fh.close
		end

		def write_to_estabs_dir(estab_file, page)
			fh = File.open("estab_inspecs/raw/#{@today}/estabs/#{estab_file}.html", "w" )
        		fh.write(page)
        	fh.close
		end

	end#class
end#module


if __FILE__ == $0
  cmd = ARGV[0]
 
  if cmd == "fetch"
    scraper = Scraper::FoodEstabs.new
	scraper.fetch
  end

  if cmd == "get_estabs"
  	scraper = Scraper::FoodEstabs.new
  	scraper.get_estab_pages
  end

  if cmd == "process_estabs"
  	scraper = Scraper::FoodEstabs.new
  	scraper.process_estabs
  end
end




