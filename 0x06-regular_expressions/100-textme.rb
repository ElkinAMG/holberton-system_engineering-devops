#!/usr/bin/env ruby

from = ARGV[0].scan(/(?:from|to):(\+?\w+)/).join(',')
flags = ARGV[0].scan(/flags:([\w+-:]*)/).join

puts from + "," + flags
