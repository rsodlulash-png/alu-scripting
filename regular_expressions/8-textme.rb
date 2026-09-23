#!/usr/bin/env ruby

input = ARGV[0]

match = input.match(/\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/)

if match
  puts "#{match[1]},#{match[2]},#{match[3]}"
end
