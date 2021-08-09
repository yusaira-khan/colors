require 'minitest/autorun'
require_relative 'color'
class ColorTest < Minitest::Test

  def test_red
    assert_equal("#ff0000",Color.new(red:255).rgb)
  end
  def test_green
    assert_equal("#00ff00",Color.new(green:255).rgb)
  end
end
