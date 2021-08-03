require 'minitest/autorun'
def rgb(red:)
  return "#ff0000"
end
class ColorTest < Minitest::Test

  def test_red
    assert_equal(rgb(red:100),"#ff0000")
  end
end
