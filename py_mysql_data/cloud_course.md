


### 1、 大主题 (co_big_theme) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 名称 | 
 | cover_image | varchar(128) | YES | 封面图片 | 
 | school_stage_id | varchar(64) | YES | 学段ID | 
 | grade_id | varchar(64) | YES | 年级ID | 
 | term_id | varchar(64) | YES | 学期ID | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 2、 教材版本 (co_book_version) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 版本名称 | 
 | school_stage_id | varchar(64) | YES | 学段ID | 
 | subject_id | varchar(64) | YES | 科目ID | 
 | grade_id | varchar(64) | YES | 年级ID | 
 | volume_id | varchar(64) | YES | 上下册ID | 
 | list_sort | int(11) | YES | 顺序 | 
 | cover_image | varchar(128) | YES | 封面图片 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 3、 章节 (co_chapter) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | book_version_id | varchar(64) | NO | 教材版本ID | 
 | name | varchar(64) | YES | 章节名称 | 
 | parent_id | varchar(64) | YES | 父级编号 | 
 | parent_codes | varchar(500) | YES | 所有父级编号 | 
 | tree_level | int(11) | YES | 层级 | 
 | tree_sort | int(11) | YES | 次序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 4、 课程 (co_course) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | course_code | bigint(11) | NO | 课程ID(策划看) | 
 | name | varchar(64) | YES | 名称 | 
 | cover_image | varchar(128) | YES | 封面图片 | 
 | school_stage_type | varchar(10) | YES | 学段类型 | 
 | school_stage_id | varchar(64) | YES | 学段ID | 
 | grade_id | varchar(64) | YES | 年级ID | 
 | subject_ids | varchar(500) | YES | 科目ID | 
 | publish_vesion | varchar(10) | YES | 上架版本 | 
 | status_ios | varchar(10) | YES | IOS上架状态 | 
 | status_android | varchar(10) | YES | 安卓上架状态 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 5、 普教关联课程 (co_course_pj) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | course_id | varchar(64) | NO | 课程ID | 
 | volume_id | varchar(64) | YES | 上下册ID | 
 | book_version_id | varchar(64) | YES | 教材ID | 
 | chapter_ids | varchar(500) | YES | 章节ID组 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 6、 课程关联资源 (co_course_resource) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | course_id | varchar(64) | NO | 课程ID | 
 | resource_code | bigint(64) | NO | 资源编号 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 7、 幼教关联课程 (co_course_yj) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | course_id | varchar(64) | NO | 课程ID | 
 | term_id | varchar(64) | YES | 学期ID | 
 | big_theme_id | varchar(64) | YES | 大主题ID | 
 | small_theme_id | varchar(64) | YES | 小主题ID | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 8、 年级 (co_grade) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | stage_id | varchar(64) | NO | 学段ID | 
 | name | varchar(64) | YES | 名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 9、 学段 (co_school_stage) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | type | varchar(10) | YES | 学段类型（1：幼教，2：普教） | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 10、 小主题 (co_small_theme) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 名称 | 
 | cover_image | varchar(128) | YES | 封面图片 | 
 | big_theme_id | varchar(64) | YES | 大主题ID | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 11、 科目 (co_subject) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | stage_ids | varchar(255) | NO | 学段ID组 | 
 | stage_values | varchar(255) | YES | 学段名称组 | 
 | json_params | varchar(255) | YES | Json字符串 | 
 | name | varchar(64) | YES | 名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 12、 学期 (co_term) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 13、 上下册 (co_volume) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 14、 组件 (res_assembly) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | assembly_code | bigint(11) | NO | 组件ID(策划看ID) | 
 | name | varchar(64) | YES | 名称 | 
 | version | varchar(64) | YES | 版本 | 
 | school_stage_id | varchar(64) | YES | 学段ID | 
 | assembly_type_id | varchar(64) | YES | 组件类型ID | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 15、 组件类型 (res_assembly_type) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | name | varchar(64) | YES | 名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 16、 公共资源 (res_client_resource) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | resource_code | bigint(20) | NO | 资源编号 | 
 | resource_url | varchar(255) | YES | 资源包地址 | 
 | name | varchar(64) | YES | 名称 | 
 | version | varchar(64) | YES | 资源版本 | 
 | app_version | varchar(64) | YES | APP版本号 | 
 | platform_type | varchar(10) | YES | 平台类型 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 17、 资源 (res_resource) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | resource_code | bigint(20) | NO | 资源编号 | 
 | assembly_id | varchar(64) | YES | 组件ID | 
 | resource_url | varchar(255) | YES | 资源包地址 | 
 | file_name | varchar(255) | YES | 资源包名 | 
 | name | varchar(64) | YES | 名称 | 
 | version | varchar(64) | YES | 资源版本 | 
 | platform_type | varchar(10) | YES | 平台类型 | 
 | list_sort | int(11) | YES | 顺序 | 
 | publish_status | varchar(10) | YES | 发布状态 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 18、 行政区划 (sys_area) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | area_code | varchar(100) | NO | 区域编码 | 
 | parent_code | varchar(64) | NO | 父级编号 | 
 | parent_codes | varchar(500) | NO | 所有父级编号 | 
 | tree_sort | decimal(10,0) | NO | 本级排序号（升序） | 
 | tree_sorts | varchar(255) | NO | 所有级别排序号 | 
 | tree_leaf | char(1) | NO | 是否最末级 | 
 | tree_level | decimal(4,0) | NO | 层次级别 | 
 | tree_names | varchar(255) | NO | 全节点名 | 
 | area_name | varchar(64) | NO | 区域名称 | 
 | area_type | char(1) | YES | 区域类型 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 19、 机构表 (sys_company) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | parent_id | varchar(64) | YES | 父级编号 | 
 | parent_codes | varchar(500) | YES | 所有父级编号 | 
 | tree_level | int(11) | YES | 层级 | 
 | tree_sort | int(255) | YES | 次序 | 
 | name | varchar(64) | YES | 机构名称 | 
 | company_code | varchar(64) | YES | 机构代码 | 
 | company_type | varchar(20) | YES | 机构类型 | 
 | phone | varchar(20) | YES | 联系方式 | 
 | address | varchar(128) | YES | 地址 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 20、 部门表 (sys_department) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | company_id | varchar(64) | YES | 所属组织 | 
 | name | varchar(64) | YES | 部门名称 | 
 | list_sort | int(11) | YES | 顺序 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 21、 菜单表 (sys_menu) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | bigint(64) | NO | 菜单ID | 
 | parent_id | varchar(64) | NO | 父级编号 | 
 | parent_codes | varchar(128) | NO | 所有父级编号 | 
 | tree_sort | decimal(10,0) | NO | 本级排序号（升序） | 
 | tree_level | decimal(4,0) | NO | 层次级别 | 
 | menu_name | varchar(64) | NO | 菜单名称 | 
 | menu_type | char(1) | NO | 菜单类型（1菜单 2权限） | 
 | menu_href | varchar(255) | YES | 链接 | 
 | menu_icon | varchar(64) | YES | 图标 | 
 | permission | varchar(64) | YES | 权限标识 | 
 | is_common | varchar(10) | YES | 是否公共菜单 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 22、 应该模块表 (sys_module) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | module_name | varchar(64) | YES | 名称 | 
 | module_key | varchar(64) | YES | 应用key | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 23、 角色表 (sys_role) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 角色ID | 
 | role_name | varchar(64) | NO | 角色名称 | 
 | role_type | varchar(64) | YES | 角色分类（高管、中层、基层、其它） | 
 | role_sort | decimal(10,0) | YES | 角色排序（升序） | 
 | is_sys | char(1) | YES | 系统内置（1是 0否） | 
 | company_id | varchar(64) | YES | 所属组织ID | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 24、 角色与菜单关联表 (sys_role_menu) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | role_id | varchar(64) | NO | 角色ID | 
 | menu_id | varchar(64) | NO | 菜单ID | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 25、 用户表 (sys_user) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | id | varchar(64) | NO | 主键 | 
 | login_code | varchar(64) | YES | 登录账号 | 
 | user_name | varchar(64) | NO | 用户名称 | 
 | password | varchar(64) | NO | 登录密码 | 
 | email | varchar(64) | YES | 电子邮箱 | 
 | mobile | varchar(20) | YES | 手机号码 | 
 | sex | char(1) | YES | 用户性别 | 
 | avatar | varchar(255) | YES | 头像路径 | 
 | user_type | varchar(16) | NO | 用户类型 | 
 | company_id | varchar(64) | NO | 所属组织ID | 
 | department_id | varchar(64) | YES | 所属部门ID | 
 | validity_time | datetime | YES | 账号有效期 | 
 | parent_login_code | varchar(64) | YES | 父账号 | 
 | company_num | int(11) | YES | 机构数量 | 
 | limit_num | int(11) | YES | 拥有账号数量 | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 



### 26、 用户与角色关联表 (sys_user_role) 
 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
   | ---- | ---- | ---- | ---- | 
 | user_id | varchar(64) | NO | 用户ID | 
 | role_id | varchar(64) | NO | 角色ID | 
 | status | varchar(10) | YES | 状态 | 
 | create_by | varchar(64) | YES | 创建者 | 
 | create_time | datetime | YES | 创建时间 | 
 | modify_by | varchar(64) | YES | 更新者 | 
 | modify_time | datetime | YES | 更新时间 | 
 | remarks | varchar(500) | YES | 备注信息 | 
