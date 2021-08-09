class Color
  def initialize(red:0,green:0,blue:0)
    @red=normalize red
    @green=normalize green
    @blue=normalize blue
  end
  def hex
    return "##{to_hex @red}#{to_hex @green}#{to_hex @blue}"
  end
  def rgb
    hex
  end
  def to_hex(val)
    val.to_s(16).rjust(2,"0")
  end
  def normalize(val)
    if val.is_a? Float
      if val.between?(0.0,1.0)
        val=val*255
      end
      val.round
    else
      val
    end
  end
end