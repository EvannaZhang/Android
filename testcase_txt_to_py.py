import json
from pathlib import Path

# change test case txt folder path (ctest_xx.txt) here!
# in group server (10.20.48.184), location: /home/jerrylu/docker_pipe/tests/ctest
data_path = r"C:\Others\JupyterLabPlayground\inno_proj\testcase_txt_to_py\data"

output_dir = Path("output")
if not output_dir.exists():
    print("[*] no output dir, creating...")
    output_dir.mkdir()



pre = """
from time import sleep

from appium import webdriver
import logging

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

def test_function(remote_addr='http://localhost:4723/wd/hub', desired_caps=None, write_name="default"):
    if desired_caps is None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'de.danoeh.antennapod'
        desired_caps['appActivity'] = 'de.danoeh.antennapod.activity.SplashActivity'
        desired_caps['eventTimings'] = True
        #desired_caps['app'] = '/Users/evanna/Desktop/lizi/app-free-release-signed.apk'
        logging.info("logging app...")

    driver = webdriver.Remote(remote_addr, desired_caps)
    
    # test begin ---------------------------------
"""

post="""

    # test end ------------------------------------
    # get the last page source
    page_source = driver.page_source
    print("{*} page_source get, len", len(page_source))
    with open(f"page_source_{write_name}.xml","w",encoding="utf8") as f:
        f.write(page_source)
"""


for file in Path(data_path).iterdir():
    print(f"[*] converting {str(file)}")
    with open(file, "r", encoding="utf8") as f:
        content = f.readlines()
    for line in content:
        if line.startswith("test"):
            print(f"[*] processing {str(file)} -> {str(line).strip()}")
            buffer = []
            testcase_name = line.strip().replace(":","")
            do_record = True
            continue
        if do_record and not line.startswith("native_APIs:"):
            buffer.append("\t"+line)
        if do_record and line.startswith("native_APIs"):
            do_record = False
            with open(f"output/testcase_{file.stem}_{testcase_name}.py","w",encoding="utf8") as f:
                f.write(pre)
                f.writelines(buffer)
                f.write(post)

print("[*] done!")