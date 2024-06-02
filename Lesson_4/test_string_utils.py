import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitalize():
    """POSITIVE"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("123") == "123"
    """NEGATIVE"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("12345тест") == "12345тест"


@pytest.mark.parametrize("input_string, expected_output",[
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123", "123"),
    ("", ""),
    (" ", " "),
    ("12345тест", "12345тест")
    ])
def test_capitalize(input_string, expected_output):
    assert utils.capitilize(input_string) == expected_output

def test_trim():
    """POSITIVE"""
    assert utils.trim("  skypro") == "skypro"
    assert utils.trim("  hello world") == "hello world"
    assert utils.trim("  SKY ") == "SKY "
    """NEGATIVE"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"


@pytest.mark.parametrize('string, delimeter, result', [
    ("яблоко,банан,апельсин", ",", ["яблоко","банан","апельсин"]),
    ("1,2,3,4,5",",",["1","2","3","4","5"]),
    ("*@$@%@&", "@",["*", "$", "%", "&"]),
    ("", None,[]),  
    ("1,2,3,45", None, ["1","2","3","45"]),                                                                                      
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
     res = utils.to_list(string)
    else:
     res = utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string,symbol,result',[
   ("корень","к","орень"),
   ("Женя","н","Жея"),
   ("Море","М","оре"),
   ("123","1","23"),
   ("Красная Площадь"," ","КраснаяПлощадь"),
   ("ножик","з","ножик"),
   ("","",""),
   ("","с",""),
   ("кофе","","кофе"),
   ("зелень "," ","зелень"),
])
def test_delete_symbol(string,symbol,result):
   res = utils.delete_symbol(string,symbol)
   assert res == result
   

@pytest.mark.parametrize('string,symbol,result',[
   ("тюлень","т",True),
   ("","",True),
   ("Самара","С",True),
   ("Music","M",True),
   ("Картина-Корзина","К",True),
   ("567","5",True),
   ("Маня","м",False),
   ("","@",False),
   ("кофе","К",False),
   ("звук ","и",False),
])
def test_start_with(string,symbol,result):
   res = utils.starts_with(string,symbol)
   assert res == result

@pytest.mark.parametrize('string,symbol,result',[
   ("Мария","я",True),
   ("МариЯ","Я",True),
   ("МариЯ","я",False),
   ("Мария","i",False),
   ("","",True),
   ("","&",False),
   ("Мария ","я",False),
])
def test_end_with(string,symbol,result):
   res = utils.end_with(string,symbol)
   assert res == result

@pytest.mark.parametrize('string,result',[
   ("",True),
   (" ",True),
   ("  ",True),
   ("не пусто",False),
   (" не пусто с пробелом",False),
   ("345",False),
])
def test_is_empty(string,result):
   res = utils.is_empty(string)
   assert res == result

@pytest.mark.parametrize('lst,joiner,result',[
   (["s","o","k"],",","s,o,k"),
   ([1,2,3,4,5],None,"1,2,3,4,5"),
   (["Раз","Два"],"-","Раз-Два"),
   ([],None,""),
   ([],",",""),
   ([],"торт","")
])
def test_list_to_string(lst,joiner,result):
   if joiner == None:
      res = utils.list_to_string(lst)
    else:
      res = utils.list_to_string(lst,joiner)
    assert res == result