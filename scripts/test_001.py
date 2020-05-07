import pytest,allure




class Test_Abc:
    @allure.testcase("http://www.baidu.com/test_002", "测试用例地址")
    @allure.step(title="第一个测试")
    @allure.severity(allure.severity_level.BLOCKER)

    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_abc_001(self):
        allure.attach("这是一个描述","试一下")
        assert 1

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_abc_002(self):
        allure.attach("这是第二个一个描述","试一下2")
        assert 1

    # def test_cdf_002(self):
    #     assert 0

# if __name__ == '__main__':
    # pytest.main(["-s", "-q", "--alluredir", "/Users/liudan/PycharmProjects/Test_Allure/report", "/Users/liudan/PycharmProjects/Test_Allure/scripts/test_001.py"])    # pytest.main(["-m", "login", "-s", "-q", "--alluredir", "/Users/liudan/PycharmProjects/Test_Allure/report"])


    # 将测试报告转为html格式
    # split = 'allure ' + 'generate ' + './report ' + '-o ' + './report/html ' + '--clean'
    # os.system('cd /Users/liudan/PycharmProjects/Test_Allure/report')
    # os.system(split)
    # print(split)
