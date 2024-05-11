#!/usr/bin/env ruby
#
ARGF.each do |line|
  sender = line.scan(/from:([^\]]+)/).join
  receiver = line.scan(/to:([^\]]+)/).join
  flags = line.scan(/flags:([^\]]+)/).join

  puts "#{sender},#{receiver},#{flags}"
end
