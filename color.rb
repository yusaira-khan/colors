class Color
  def initialize(red:0,green:0,blue:0)
    @red=red
    @green=green
    @blue=blue
  end
  def rgb
    return "##{percentage_to_hex @red}#{percentage_to_hex @green}#{percentage_to_hex @blue}"
  end
  def percentage_to_hex(perc)
    (perc.to_f/100*255).round.to_s(16).rjust(2,"0")
  end
end