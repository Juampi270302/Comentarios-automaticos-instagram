from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from dotenv import load_dotenv
from dotenv import dotenv_values
from user_extractor import extractor_name


def main():
    load_dotenv("credentials.env")

    target_post = "https://www.instagram.com/p/Cpu6lKIO8MZ/?img_index=1"
    coment_text = extractor_name()

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")

    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    config = dotenv_values("credentials.env")

    username_input.send_keys(config.get("USERNAME"))
    password_input.send_keys(config.get("PASSWORD"))
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.get(target_post)
    time.sleep(5)
    for i in range(0, len(coment_text)):
        try:
            if i == 0:
                comment_field = driver.find_element(By.XPATH,
                                                    '//textarea[@class="x1i0vuye xvbhtw8 x1ejq31n xd10rxx x1sy0etr x17r0tee x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm"]')
                ActionChains(driver).move_to_element(comment_field).click(comment_field).perform()
            comment_field = driver.find_element(By.XPATH,
                                                '//textarea[@class="x1i0vuye xvbhtw8 x1ejq31n xd10rxx x1sy0etr x17r0tee x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm focus-visible"]')
            comment_field.send_keys(coment_text[i])
            comment_field.send_keys(Keys.RETURN)
            print("Comentario publicado con éxito.")
        except Exception as e:
            print(f"Error al comentar: {e}")
        time.sleep(5)

    driver.quit()


if __name__ == "__main__":
    main()

