import allure

@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user authentication tokens"):
        ...
    with allure.step("Create new API client"):
        ...

@allure.step("Create course with title {title}")
def create_course (title: str):
    ...

@allure.step("Delete course")
def delete_course():
    ...

def test_feature():
    build_api_client()
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwrights")
    delete_course()