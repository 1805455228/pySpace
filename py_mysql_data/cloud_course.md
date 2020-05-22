


### 1�� ������ (co_big_theme) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | ���� | 
 | cover_image | varchar(128) | YES | ����ͼƬ | 
 | school_stage_id | varchar(64) | YES | ѧ��ID | 
 | grade_id | varchar(64) | YES | �꼶ID | 
 | term_id | varchar(64) | YES | ѧ��ID | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 2�� �̲İ汾 (co_book_version) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | �汾���� | 
 | school_stage_id | varchar(64) | YES | ѧ��ID | 
 | subject_id | varchar(64) | YES | ��ĿID | 
 | grade_id | varchar(64) | YES | �꼶ID | 
 | volume_id | varchar(64) | YES | ���²�ID | 
 | list_sort | int(11) | YES | ˳�� | 
 | cover_image | varchar(128) | YES | ����ͼƬ | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 3�� �½� (co_chapter) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | book_version_id | varchar(64) | NO | �̲İ汾ID | 
 | name | varchar(64) | YES | �½����� | 
 | parent_id | varchar(64) | YES | ������� | 
 | parent_codes | varchar(500) | YES | ���и������ | 
 | tree_level | int(11) | YES | �㼶 | 
 | tree_sort | int(11) | YES | ���� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 4�� �γ� (co_course) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | course_code | bigint(11) | NO | �γ�ID(�߻���) | 
 | name | varchar(64) | YES | ���� | 
 | cover_image | varchar(128) | YES | ����ͼƬ | 
 | school_stage_type | varchar(10) | YES | ѧ������ | 
 | school_stage_id | varchar(64) | YES | ѧ��ID | 
 | grade_id | varchar(64) | YES | �꼶ID | 
 | subject_ids | varchar(500) | YES | ��ĿID | 
 | publish_vesion | varchar(10) | YES | �ϼܰ汾 | 
 | status_ios | varchar(10) | YES | IOS�ϼ�״̬ | 
 | status_android | varchar(10) | YES | ��׿�ϼ�״̬ | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 5�� �ս̹����γ� (co_course_pj) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | course_id | varchar(64) | NO | �γ�ID | 
 | volume_id | varchar(64) | YES | ���²�ID | 
 | book_version_id | varchar(64) | YES | �̲�ID | 
 | chapter_ids | varchar(500) | YES | �½�ID�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 6�� �γ̹�����Դ (co_course_resource) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | course_id | varchar(64) | NO | �γ�ID | 
 | resource_code | bigint(64) | NO | ��Դ��� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 7�� �׽̹����γ� (co_course_yj) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | course_id | varchar(64) | NO | �γ�ID | 
 | term_id | varchar(64) | YES | ѧ��ID | 
 | big_theme_id | varchar(64) | YES | ������ID | 
 | small_theme_id | varchar(64) | YES | С����ID | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 8�� �꼶 (co_grade) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | stage_id | varchar(64) | NO | ѧ��ID | 
 | name | varchar(64) | YES | ���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 9�� ѧ�� (co_school_stage) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | ���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | type | varchar(10) | YES | ѧ�����ͣ�1���׽̣�2���ս̣� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 10�� С���� (co_small_theme) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | ���� | 
 | cover_image | varchar(128) | YES | ����ͼƬ | 
 | big_theme_id | varchar(64) | YES | ������ID | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 11�� ��Ŀ (co_subject) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | stage_ids | varchar(255) | NO | ѧ��ID�� | 
 | stage_values | varchar(255) | YES | ѧ�������� | 
 | json_params | varchar(255) | YES | Json�ַ��� | 
 | name | varchar(64) | YES | ���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 12�� ѧ�� (co_term) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | ���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 13�� ���²� (co_volume) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | ���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 14�� ��� (res_assembly) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | assembly_code | bigint(11) | NO | ���ID(�߻���ID) | 
 | name | varchar(64) | YES | ���� | 
 | version | varchar(64) | YES | �汾 | 
 | school_stage_id | varchar(64) | YES | ѧ��ID | 
 | assembly_type_id | varchar(64) | YES | �������ID | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 15�� ������� (res_assembly_type) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | name | varchar(64) | YES | ���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 16�� ������Դ (res_client_resource) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | resource_code | bigint(20) | NO | ��Դ��� | 
 | resource_url | varchar(255) | YES | ��Դ����ַ | 
 | name | varchar(64) | YES | ���� | 
 | version | varchar(64) | YES | ��Դ�汾 | 
 | app_version | varchar(64) | YES | APP�汾�� | 
 | platform_type | varchar(10) | YES | ƽ̨���� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 17�� ��Դ (res_resource) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | resource_code | bigint(20) | NO | ��Դ��� | 
 | assembly_id | varchar(64) | YES | ���ID | 
 | resource_url | varchar(255) | YES | ��Դ����ַ | 
 | file_name | varchar(255) | YES | ��Դ���� | 
 | name | varchar(64) | YES | ���� | 
 | version | varchar(64) | YES | ��Դ�汾 | 
 | platform_type | varchar(10) | YES | ƽ̨���� | 
 | list_sort | int(11) | YES | ˳�� | 
 | publish_status | varchar(10) | YES | ����״̬ | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 18�� �������� (sys_area) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | area_code | varchar(100) | NO | ������� | 
 | parent_code | varchar(64) | NO | ������� | 
 | parent_codes | varchar(500) | NO | ���и������ | 
 | tree_sort | decimal(10,0) | NO | ��������ţ����� | 
 | tree_sorts | varchar(255) | NO | ���м�������� | 
 | tree_leaf | char(1) | NO | �Ƿ���ĩ�� | 
 | tree_level | decimal(4,0) | NO | ��μ��� | 
 | tree_names | varchar(255) | NO | ȫ�ڵ��� | 
 | area_name | varchar(64) | NO | �������� | 
 | area_type | char(1) | YES | �������� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 19�� ������ (sys_company) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | parent_id | varchar(64) | YES | ������� | 
 | parent_codes | varchar(500) | YES | ���и������ | 
 | tree_level | int(11) | YES | �㼶 | 
 | tree_sort | int(255) | YES | ���� | 
 | name | varchar(64) | YES | �������� | 
 | company_code | varchar(64) | YES | �������� | 
 | company_type | varchar(20) | YES | �������� | 
 | phone | varchar(20) | YES | ��ϵ��ʽ | 
 | address | varchar(128) | YES | ��ַ | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 20�� ���ű� (sys_department) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | company_id | varchar(64) | YES | ������֯ | 
 | name | varchar(64) | YES | �������� | 
 | list_sort | int(11) | YES | ˳�� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 21�� �˵��� (sys_menu) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | bigint(64) | NO | �˵�ID | 
 | parent_id | varchar(64) | NO | ������� | 
 | parent_codes | varchar(128) | NO | ���и������ | 
 | tree_sort | decimal(10,0) | NO | ��������ţ����� | 
 | tree_level | decimal(4,0) | NO | ��μ��� | 
 | menu_name | varchar(64) | NO | �˵����� | 
 | menu_type | char(1) | NO | �˵����ͣ�1�˵� 2Ȩ�ޣ� | 
 | menu_href | varchar(255) | YES | ���� | 
 | menu_icon | varchar(64) | YES | ͼ�� | 
 | permission | varchar(64) | YES | Ȩ�ޱ�ʶ | 
 | is_common | varchar(10) | YES | �Ƿ񹫹��˵� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 22�� Ӧ��ģ��� (sys_module) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | module_name | varchar(64) | YES | ���� | 
 | module_key | varchar(64) | YES | Ӧ��key | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 23�� ��ɫ�� (sys_role) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ��ɫID | 
 | role_name | varchar(64) | NO | ��ɫ���� | 
 | role_type | varchar(64) | YES | ��ɫ���ࣨ�߹ܡ��в㡢���㡢������ | 
 | role_sort | decimal(10,0) | YES | ��ɫ�������� | 
 | is_sys | char(1) | YES | ϵͳ���ã�1�� 0�� | 
 | company_id | varchar(64) | YES | ������֯ID | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 24�� ��ɫ��˵������� (sys_role_menu) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | role_id | varchar(64) | NO | ��ɫID | 
 | menu_id | varchar(64) | NO | �˵�ID | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 25�� �û��� (sys_user) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | ���� | 
 | login_code | varchar(64) | YES | ��¼�˺� | 
 | user_name | varchar(64) | NO | �û����� | 
 | password | varchar(64) | NO | ��¼���� | 
 | email | varchar(64) | YES | �������� | 
 | mobile | varchar(20) | YES | �ֻ����� | 
 | sex | char(1) | YES | �û��Ա� | 
 | avatar | varchar(255) | YES | ͷ��·�� | 
 | user_type | varchar(16) | NO | �û����� | 
 | company_id | varchar(64) | NO | ������֯ID | 
 | department_id | varchar(64) | YES | ��������ID | 
 | validity_time | datetime | YES | �˺���Ч�� | 
 | parent_login_code | varchar(64) | YES | ���˺� | 
 | company_num | int(11) | YES | �������� | 
 | limit_num | int(11) | YES | ӵ���˺����� | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 



### 26�� �û����ɫ������ (sys_user_role) 
 | �ֶ����� | �������� | �Ƿ�Ϊ�� | �ֶ�˵�� |
   | ---- | ---- | ---- | ---- | 
 | user_id | varchar(64) | NO | �û�ID | 
 | role_id | varchar(64) | NO | ��ɫID | 
 | status | varchar(10) | YES | ״̬ | 
 | create_by | varchar(64) | YES | ������ | 
 | create_time | datetime | YES | ����ʱ�� | 
 | modify_by | varchar(64) | YES | ������ | 
 | modify_time | datetime | YES | ����ʱ�� | 
 | remarks | varchar(500) | YES | ��ע��Ϣ | 
