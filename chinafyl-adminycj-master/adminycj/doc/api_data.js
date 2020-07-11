define({ "api": [
  {
    "type": "post",
    "url": "api/user/addUser",
    "title": "添加用户账号",
    "version": "0.0.1",
    "name": "add_user",
    "group": "User",
    "description": "<p>添加用户账号</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "account",
            "description": "<p>(必须)    账号名(手机号11位)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>(必须)    账户密码</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "user_name",
            "description": "<p>(必须)    用户真实姓名</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    所属专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须)   所属稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    用户账号等级id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"account\":\"18125412365\",\n    \"password\":\"132456\",\n    \"user_name\":\"范若若\",\n    \"station_id\":2,\n    \"department_id\":2,\n    \"role_id\":2\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"用户添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"PARAMETER_CHECK_ERROR\",\n    \"data\": null,\n    \"message\": \"required key not provided @ data['role_id']\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/addUser"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/user/delUser",
    "title": "删除用户账号",
    "version": "0.0.1",
    "name": "delete_user",
    "group": "User",
    "description": "<p>删除用户账号</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "account",
            "description": "<p>(必须)    账号名(手机号11位)</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    用户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"user_id\":4,\n    \"account\":\"18125412365\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"用户删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/delUser"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/user/getAllstationboss",
    "title": "直接通过get查询所有专卖局负责人，使用分页",
    "version": "0.0.1",
    "name": "getAllstationboss",
    "group": "User",
    "description": "<p>直接通过get查询所有专卖局负责人</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "  {\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 7,\n                \"role_id\": 2,\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\",\n                \"account\": \"18125412365\",\n                \"password\": \"132456\",\n                \"user_name\": \"YQY333\",\n                \"department_id\": 2\n            },\n            {\n                \"id\": 52,\n                \"role_id\": 2,\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\",\n                \"account\": \"YQY\",\n                \"password\": \"123456\",\n                \"user_name\": \"杨秋月\",\n                \"department_id\": 1\n            },\n            {\n                \"id\": 13,\n                \"role_id\": 2,\n                \"station_id\": 2,\n                \"station_name\": \"义乌市专卖局\",\n                \"account\": \"55555555555\",\n                \"password\": \"132456\",\n                \"user_name\": \"夏季\",\n                \"department_id\": 2\n            },\n            {\n                \"id\": 10,\n                \"role_id\": 2,\n                \"station_id\": 2,\n                \"station_name\": \"义乌市专卖局\",\n                \"account\": \"11177777221\",\n                \"password\": \"132456\",\n                \"user_name\": \"范若若\",\n                \"department_id\": 2\n            },\n            {\n                \"id\": 8,\n                \"role_id\": 2,\n                \"station_id\": 2,\n                \"station_name\": \"义乌市专卖局\",\n                \"account\": \"11\",\n                \"password\": \"132456\",\n                \"user_name\": \"范若若\",\n                \"department_id\": 2\n            },\n            {\n                \"id\": 17,\n                \"role_id\": 2,\n                \"station_id\": 2,\n                \"station_name\": \"义乌市专卖局\",\n                \"account\": \"44444444444\",\n                \"password\": \"123456\",\n                \"user_name\": \"范雨涵\",\n                \"department_id\": 2\n            },\n            {\n                \"id\": 53,\n                \"role_id\": 2,\n                \"station_id\": 4,\n                \"station_name\": \"东阳市专卖局\",\n                \"account\": \"luxun\",\n                \"password\": \"123456\",\n                \"user_name\": \"鲁迅\",\n                \"department_id\": 1\n            },\n            {\n                \"id\": 67,\n                \"role_id\": 2,\n                \"station_id\": 8,\n                \"station_name\": \"永康市专卖局\",\n                \"account\": \"1899\",\n                \"password\": \"1899\",\n                \"user_name\": \"我的名字叫做难\",\n                \"department_id\": 19\n            }\n        ],\n        \"count\": 11\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/getAllstationboss"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/user/getUserBysomeroleid",
    "title": "稽查人员管理",
    "version": "0.0.1",
    "name": "getUserBysomeroleid",
    "group": "User",
    "description": "<p>稽查人员管理,此处使用了分页功能，page参数指定页数，per_page参数指定每页显示多少内容</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(可选)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(可选)    稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"department_id\":1,\n    \"role_id\":3,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 1,\n                \"role_id\": 4,\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\",\n                \"depart_name\": \"二所一片\",\n                \"account\": \"10010001000\",\n                \"password\": \"123456\",\n                \"user_name\": \"杨秋月\",\n                \"department_id\": 1\n            }\n        ],\n        \"count\": 1\n    },\n    \"message\": \" \"\n}\n                }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/getUserBysomeroleid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/user/getUserInfoByid",
    "title": "通过用户id获取用户详细信息",
    "version": "0.0.1",
    "name": "getUserInfoByid",
    "group": "User",
    "description": "<p>通过用户id获取用户详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    用户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"user_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " {\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"account\": \"10010001000\",\n            \"password\": \"123456\",\n            \"role_id\": 4,\n            \"department_id\": 1,\n            \"depart_name\": \"二所一片\",\n            \"station_id\": 1,\n            \"station_name\": \"金华市专卖局\",\n            \"user_name\": \"杨秋月\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/getUserInfoByid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/user/getUserInfoByname",
    "title": "通过用户姓名获取用户详细信息--分页—--杨",
    "version": "0.0.1",
    "name": "getUserInfoByname",
    "group": "User",
    "description": "<p>通过用户姓名获取用户详细信息--分页—--杨</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "user_name",
            "description": "<p>(必须)    用户名</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"user_name\":\"杨秋月\",\n    \"role_id\":2,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " {\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 8,\n                \"account\": \"11\",\n                \"password\": \"132456\",\n                \"role_id\": 2,\n                \"department_id\": 2,\n                \"depart_name\": \"二所二片\",\n                \"station_id\": 2,\n                \"station_name\": \"义乌市专卖局\",\n                \"user_name\": \"范若若\"\n            },\n            {\n                \"id\": 10,\n                \"account\": \"11177777221\",\n                \"password\": \"132456\",\n                \"role_id\": 2,\n                \"department_id\": 2,\n                \"depart_name\": \"二所二片\",\n                \"station_id\": 2,\n                \"station_name\": \"义乌市专卖局\",\n                \"user_name\": \"范若若\"\n            }\n        ],\n        \"count\": 2\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/getUserInfoByname"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/user/getUserinfoByroleidSearchlike",
    "title": "稽查人员模糊查询--吴",
    "version": "0.0.1",
    "name": "getUserinfoByroleidSearchlike",
    "group": "User",
    "description": "<p>稽查人员模糊查询,模糊查询未使用分页，角色id为1，可以获取所有符合条件的数据，角色id为2（局长），可以获取本局的数据，角色id为3或者4，可以获取稽查所内稽查人员信息数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(可选)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(可选)    稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "key",
            "description": "<p>(必须)    以姓名或者账号作为搜索条件</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"role_id\":1,\n    \"department_id\":1,\n    \"key\":\"杨\",\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"role_id\":2,\n    \"department_id\":1,\n    \"key\":\"杨\"\n}",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"role_id\":3,\n    \"department_id\":1,\n    \"key\":\"杨\"\n}",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"role_id\":4,\n    \"department_id\":1,\n    \"key\":\"杨\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "   \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 5,\n            \"role_id\": 1,\n            \"station_id\": 1,\n            \"depart_name\": \"二所二片\",\n            \"account\": \"50050005000\",\n            \"password\": \"123456\",\n            \"user_name\": \"胡杨\",\n            \"department_id\": 2\n        },\n        {\n            \"id\": 1,\n            \"role_id\": 4,\n            \"station_id\": 1,\n            \"depart_name\": \"二所一片\",\n            \"account\": \"10010001000\",\n            \"password\": \"123456\",\n            \"user_name\": \"杨秋月\",\n            \"department_id\": 1\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 5,\n            \"role_id\": 1,\n            \"station_id\": 1,\n            \"depart_name\": \"二所二片\",\n            \"account\": \"50050005000\",\n            \"password\": \"123456\",\n            \"user_name\": \"胡杨\",\n            \"department_id\": 2\n        },\n        {\n            \"id\": 1,\n            \"role_id\": 4,\n            \"station_id\": 1,\n            \"depart_name\": \"二所一片\",\n            \"account\": \"10010001000\",\n            \"password\": \"123456\",\n            \"user_name\": \"杨秋月\",\n            \"department_id\": 1\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"role_id\": 4,\n            \"station_id\": 1,\n            \"depart_name\": \"二所一片\",\n            \"account\": \"10010001000\",\n            \"password\": \"123456\",\n            \"user_name\": \"杨秋月\",\n            \"department_id\": 1\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"role_id\": 4,\n            \"station_id\": 1,\n            \"depart_name\": \"二所一片\",\n            \"account\": \"10010001000\",\n            \"password\": \"123456\",\n            \"user_name\": \"杨秋月\",\n            \"department_id\": 1\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/getUserinfoByroleidSearchlike"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/user/getdepartbossByroleid",
    "title": "稽查所负责人管理",
    "version": "0.0.1",
    "name": "getdepartbossByroleid",
    "group": "User",
    "description": "<p>稽查所负责人管理,此处使用了分页功能，page参数指定页数，per_page参数指定每页显示多少内容</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"role_id\":3,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 4,\n                \"role_id\": 3,\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\",\n                \"depart_name\": \"二所一片\",\n                \"account\": \"40040004000\",\n                \"password\": \"123456\",\n                \"user_name\": \"胡适\",\n                \"department_id\": 1\n            }\n        ],\n        \"count\": 1\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/getdepartbossByroleid"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/user/login",
    "title": "用户登录",
    "version": "0.0.1",
    "name": "login",
    "group": "User",
    "description": "<p>用户登录</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "account",
            "description": "<p>(必须)    账号名(手机号11位)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>(必须)    账户密码</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"account\": \"18256894562\",\n    \"password\": \"124586\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"id\": 1,\n        \"account\": \"18256894562\",\n        \"password\": \"124586\",\n        \"user_name\": \"范闲\",\n        \"department_id\": 1,\n        \"role_id\": 2\n            },\n    \"message\": \"成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": null,\n    \"message\": \"用户名密码不匹配\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/login"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/user/reset_password",
    "title": "用户修改密码",
    "version": "0.0.1",
    "name": "reset_pass",
    "group": "User",
    "description": "<p>用户修改密码</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    用户id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password_old",
            "description": "<p>(必须)    旧密码</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>(必须)    新密码</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n\n    \"user_id\":1,\n    \"password_old\": \"124586\",\n    \"password\":\"123456\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": null,\n     \"message\": \"修改密码成功\"\n }",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n     \"sys_status\": \"FAIL\",\n     \"data\": null,\n     \"message\": \"原密码错误\"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/reset_password"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/user/modifyUserInfo",
    "title": "修改用户信息",
    "version": "0.0.1",
    "name": "user_info_put",
    "group": "User",
    "description": "<p>修改用户信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    用户id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "account",
            "description": "<p>(可选)    账号名(手机号11位)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "user_name",
            "description": "<p>(可选)    用户真实姓名</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>(可选)    账户密码</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(可选)   所属稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(可选)    用户账号等级id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(可选)    所属专卖局id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"user_id\":4,\n    \"account\":\"18125412365\",\n    \"password\":\"132459\",\n    \"user_name\":\"范若\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"用户信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user.py",
    "groupTitle": "User",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/user/modifyUserInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/case/addCase",
    "title": "添加违法案件信息",
    "version": "0.0.1",
    "name": "addCase",
    "group": "case",
    "description": "<p>添加违法案件信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "caseId",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须,零售商户表必须有此数据)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "case_date",
            "description": "<p>(可选)    案发时间</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "case_value",
            "description": "<p>(可选)    案值</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "count",
            "description": "<p>(可选)    卷烟数量（条数）</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "case_nature",
            "description": "<p>(可选)    案件性质</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_criminal",
            "description": "<p>(可选)   有无刑事处罚，True有 False没有</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "smoke_property01",
            "description": "<p>(可选)    是否为非流烟，True是 False否</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "smoke_property02",
            "description": "<p>(可选)    是否为假冒烟，True是 False否</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "smoke_property03",
            "description": "<p>(可选)    是否为走私烟，True是 False否</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"caseId\":\"541254521\",\n    \"case_date\":\"2020-04-01\",\n    \"case_value\":\"4521.12\",\n    \"count\":\"125.45\",\n    \"case_nature\":\"未在当地企业进货\",\n    \"is_criminal\":\"False\",\n    \"smoke_property01\":\"True\",\n    \"smoke_property02\":\"False\",\n    \"smoke_property03\":\"False\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"违法信息添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n     \"sys_status\": \"FAIL\",\n     \"data\": 1,\n     \"message\": \"该违法信息已被添加\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/addCase"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/delCase",
    "title": "删除违法案件信息",
    "version": "0.0.1",
    "name": "delCase",
    "group": "case",
    "description": "<p>删除违法案件信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "case_id",
            "description": "<p>(必须)    违法信息id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"case_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"违法信息删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/delCase"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/case/getAllCaseInfo",
    "title": "直接通过get方法获取所有违法案件信息",
    "version": "0.0.1",
    "name": "getAllCaseInfo",
    "group": "case",
    "description": "<p>直接通过get方法获取所有违法案件信息,此处使用了分页功能，因为是get方法，所以page参数通过访问地址访问，通过per_page指定每页显示多少条数据</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n   示例:http://39.96.52.170:5000/api/case/getAllCaseInfo?page=2&per_page=8  可以获取第二页的8条内容\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getAllCaseInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getBrandInfoByid",
    "title": "通过进货明细id查询进货明细详情",
    "version": "0.0.1",
    "name": "getBrandInfoByid",
    "group": "case",
    "description": "<p>通过进货明细id查询进货明细详情</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "brand_id",
            "description": "<p>(必须)    进货明细id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"brand_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": [\n         {\n             \"id\": 1,\n             \"purchase_id\": 1,\n             \"cigar_name\": \"中华软\",\n             \"cigar_price\": \"45.00\",\n             \"cigar_num\": 20\n         }\n     ],\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getBrandInfoByid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getCaseInfoByStoreid",
    "title": "根据店铺id获取违法案件信息",
    "version": "0.0.1",
    "name": "getCaseInfoByStoreid",
    "group": "case",
    "description": "<p>根据店铺id获取违法案件信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 231,\n                \"caseId\": \"541254521\",\n                \"store_id\": 5,\n                \"store_name\": \"金华市婺城区沈美香副食店\",\n                \"case_date\": \"2020-04-01\",\n                \"case_value\": \"4521.12\",\n                \"count\": \"125.45\",\n                \"case_nature\": \"未在当地企业进货\",\n                \"is_criminal\": false,\n                \"smoke_property01\": true,\n                \"smoke_property02\": false,\n                \"smoke_property03\": false\n            },\n            {\n                \"id\": 1,\n                \"caseId\": \"541254521\",\n                \"store_id\": 5,\n                \"store_name\": \"金华市婺城区沈美香副食店\",\n                \"case_date\": \"2020-04-01\",\n                \"case_value\": \"6666.66\",\n                \"count\": \"5000.00\",\n                \"case_nature\": \"未在当地企业进货\",\n                \"is_criminal\": true,\n                \"smoke_property01\": true,\n                \"smoke_property02\": false,\n                \"smoke_property03\": true\n            }\n        ],\n        \"count\": 2\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getCaseInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getCaseInfoByStorename",
    "title": "根据店铺名称获取违法案件信息",
    "version": "0.0.1",
    "name": "getCaseInfoByStorename",
    "group": "case",
    "description": "<p>根据店铺名称获取违法案件信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "store_name",
            "description": "<p>(必须)    零售商户名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_name\":\"金华市婺城区上古情歌副食便利店\",\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "               {\n                \"sys_status\": \"SUCCESS\",\n                \"data\": {\n                \"data\": [\n                    {\n                \"store_name\": \"金华市婺城区上古情歌副食便利店\",\n                \"id\": 233,\n                \"caseId\": \"\",\n                \"store_id\": 1532,\n                \"case_date\": \"2020-04-21\",\n                \"case_value\": \"1452.00\",\n                \"count\": \"48.00\",\n                \"case_nature\": null,\n                \"is_criminal\": false,\n                \"smoke_property01\": false,\n                \"smoke_property02\": false,\n                \"smoke_property03\": false\n            },\n            {\n                \"store_name\": \"金华市婺城区上古情歌副食便利店\",\n                \"id\": 13,\n                \"caseId\": \"\",\n                \"store_id\": 1403,\n                \"case_date\": \"2019-06-14\",\n                \"case_value\": null,\n                \"count\": \"179.00\",\n                \"case_nature\": \"涉嫌未在当地烟草专卖批发企业进货\",\n                \"is_criminal\": false,\n                \"smoke_property01\": true,\n                \"smoke_property02\": false,\n                \"smoke_property03\": false\n            }\n        ],\n        \"count\": 2\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getCaseInfoByStorename"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getCaseInfoByselect",
    "title": "根据店铺和筛选条件获取违法案件信息",
    "version": "0.0.1",
    "name": "getCaseInfoByselect",
    "group": "case",
    "description": "<p>案值和日期必须成对出现，不选择案值时，案值的两个参数是空字符串；不选择日期时，日期的两个参数必须是&quot;1988-01-01&quot;;</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "store_name",
            "description": "<p>(必须)    零售商户名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          },
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "low_case_value",
            "description": "<p>(可选)    案值的下界,案值和时间必须成对出现</p>"
          },
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "high_case_value",
            "description": "<p>(可选)    案值的上界</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": false,
            "field": "low_case_data",
            "description": "<p>(可选)    日期的下界</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": false,
            "field": "high_case_data",
            "description": "<p>(可选)    日期的上界</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n   \"store_name\":\"金华市金磐开发区汇达超市\",\n    \"page\":1,\n    \"per_page\":8,\n    \"low_case_data\":\"2001-01-01\",\n    \"high_case_data\":\"2020-10-10\",\n    \"low_case_value\":\"10\",\n    \"high_case_value\":\"500000\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n \"sys_status\": \"SUCCESS\",\n \"data\": {\n     \"data\": [\n         {\n             \"store_name\": \"金华市金磐开发区汇达超市\",\n             \"id\": 228,\n             \"caseId\": \"\",\n             \"store_id\": 1437,\n             \"case_date\": \"2017-12-18\",\n             \"case_value\": null,\n             \"count\": \"55.00\",\n             \"case_nature\": \"涉嫌未在当地烟草专卖批发企业进货\",\n             \"is_criminal\": false,\n             \"smoke_property01\": true,\n             \"smoke_property02\": false,\n             \"smoke_property03\": false\n         },\n         {\n             \"store_name\": \"金华市金磐开发区汇达超市\",\n             \"id\": 4,\n             \"caseId\": \"\",\n             \"store_id\": 1437,\n             \"case_date\": \"2017-12-18\",\n             \"case_value\": null,\n             \"count\": \"55.00\",\n             \"case_nature\": \"涉嫌未在当地烟草专卖批发企业进货\",\n             \"is_criminal\": false,\n             \"smoke_property01\": true,\n             \"smoke_property02\": false,\n             \"smoke_property03\": true\n         }\n     ],",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getCaseInfoByselect"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getPurchaseInfoByStoreid",
    "title": "根据店铺id获取进货详细信息",
    "version": "0.0.1",
    "name": "getPurchaseInfoByStoreid",
    "group": "case",
    "description": "<p>根据店铺id获取进货详细信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"id\": 1,\n                 \"store_id\": 5,\n                 \"purchase_date\": \"2020-04-04\",\n                 \"purchase_week\": 8,\n                 \"settlement_account\": \"458874554412\",\n                 \"required_count\": 122,\n                 \"average_price\": \"145.00\"\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getPurchaseInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getPurchaseInfoByid",
    "title": "通过进货记录id查询进货详细信息",
    "version": "0.0.1",
    "name": "getPurchaseInfoByid",
    "group": "case",
    "description": "<p>通过进货记录id查询进货详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "purchase_id",
            "description": "<p>(必须)    进货记录id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"purchase_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": [\n         {\n             \"id\": 1,\n             \"store_id\": 5,\n             \"purchase_date\": \"2020-04-04\",\n             \"purchase_week\": 8,\n             \"settlement_account\": \"458874554412\",\n             \"required_count\": 122,\n             \"average_price\": \"145.00\"\n         }\n     ],\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getPurchaseInfoByid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getbrandInfoByStoreid",
    "title": "根据店铺id获取进货明细详情",
    "version": "0.0.1",
    "name": "getbrandInfoByStoreid",
    "group": "case",
    "description": "<p>根据店铺id获取进货明细详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"id\": 1,\n                 \"purchase_id\": 1,\n                 \"cigar_name\": \"中华软\",\n                 \"cigar_price\": \"45.00\",\n                 \"cigar_num\": 20\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getbrandInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getbrandInfoBypurchaseid",
    "title": "根据进货表id查询进货明细详情",
    "version": "0.0.1",
    "name": "getbrandInfoBypurchaseid",
    "group": "case",
    "description": "<p>根据进货表id查询进货明细详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "purchase_id",
            "description": "<p>(必须)    进货表id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"purchase_id\":1,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"id\": 1,\n                 \"purchase_id\": 1,\n                 \"cigar_name\": \"中华软\",\n                 \"cigar_price\": \"45.00\",\n                 \"cigar_num\": 20\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getbrandInfoBypurchaseid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getcaseInfoByid",
    "title": "通过违法信息id获取违法违法信息",
    "version": "0.0.1",
    "name": "getcaseInfoByid",
    "group": "case",
    "description": "<p>通过违法信息id获取违法违法信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "case_id",
            "description": "<p>(必须)    违法信息id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"case_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"caseId\": \"541254521\",\n            \"store_id\": 5,\n            \"store_name\": \"金华市婺城区沈美香副食店\",\n            \"case_date\": \"2020-04-01\",\n            \"case_value\": \"6666.66\",\n            \"count\": \"5000.00\",\n            \"case_nature\": \"未在当地企业进货\",\n            \"is_criminal\": true,\n            \"smoke_property01\": true,\n            \"smoke_property02\": false,\n            \"smoke_property03\": true\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcaseInfoByid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getcasecigarInfoByCaseid",
    "title": "根据违法案件id获取进案件涉烟详情",
    "version": "0.0.1",
    "name": "getcasecigarInfoByCaseid",
    "group": "case",
    "description": "<p>根据违法案件id获取进案件涉烟详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "case_id",
            "description": "<p>(必须)    违法案件id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"case_id\":1,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"id\": 1,\n                 \"case_id\": 1,\n                 \"cigar_property\": {\n                     \"SMUGGLE\": \"走私烟\"\n                 },\n                 \"singlebrand_id\": 1,\n                 \"count\": \"25.00\",\n                 \"origin_area\": \"杭州\"\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcasecigarInfoByCaseid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getcasecigarInfoByStoreid",
    "title": "根据店铺id获取案件涉烟详情",
    "version": "0.0.1",
    "name": "getcasecigarInfoByStoreid",
    "group": "case",
    "description": "<p>根据店铺id获取案件涉烟详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"id\": 1,\n                 \"case_id\": 1,\n                 \"cigar_property\": {\n                     \"SMUGGLE\": \"走私烟\"\n                 },\n                 \"singlebrand_id\": 1,\n                 \"count\": \"25.00\",\n                 \"origin_area\": \"杭州\"\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcasecigarInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getcasecigarInfoByid",
    "title": "通过案件涉烟详情id查询案件涉烟详情",
    "version": "0.0.1",
    "name": "getcasecigarInfoByid",
    "group": "case",
    "description": "<p>通过案件涉烟详情id查询案件涉烟详情</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "casecigar_id",
            "description": "<p>(必须)    案件涉烟详情id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"casecigar_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": [\n         {\n             \"id\": 1,\n             \"case_id\": 1,\n             \"cigar_property\": {\n                 \"SMUGGLE\": \"走私烟\"\n             },\n             \"singlebrand_id\": 1,\n             \"count\": \"25.00\",\n             \"origin_area\": \"杭州\"\n         }\n     ],\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcasecigarInfoByid"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/case/modifyCaseInfo",
    "title": "修改违法案件信息",
    "version": "0.0.1",
    "name": "modifyCaseInfo",
    "group": "case",
    "description": "<p>修改违法案件信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "case_id",
            "description": "<p>(必须)    违法信息id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "caseId",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须,零售商户表必须有此数据)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "case_date",
            "description": "<p>(可选)    案发时间</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "case_value",
            "description": "<p>(可选)    案值</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "count",
            "description": "<p>(可选)    卷烟数量（条数）</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "case_nature",
            "description": "<p>(可选)    案件性质</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_criminal",
            "description": "<p>(可选)   有无刑事处罚，True有 False没有</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "smoke_property01",
            "description": "<p>(可选)    是否为非流烟，True是 False否</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "smoke_property02",
            "description": "<p>(可选)    是否为假冒烟，True是 False否</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "smoke_property03",
            "description": "<p>(可选)    是否为走私烟，True是 False否</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"case_id\":1,\n    \"store_id\":5,\n    \"caseId\":\"541254521\",\n    \"case_date\":\"2020-04-01\",\n    \"case_value\":\"6666.66\",\n    \"count\":\"5000\",\n    \"case_nature\":\"未在当地企业进货\",\n    \"is_criminal\":\"True\",\n    \"smoke_property01\":\"True\",\n    \"smoke_property02\":\"False\",\n    \"smoke_property03\":\"True\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"违法信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "case",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/modifyCaseInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/DelCaseidInfo",
    "title": "删除某个案件编号的全部信息",
    "version": "0.0.1",
    "name": "DelCaseidInfo",
    "group": "excel导入导出",
    "description": "<p>删除某个案件编号的全部信息,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"199821225455\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/DelCaseidInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/ScanCodeUpload",
    "title": "扫码获取32位码录入数据库",
    "version": "0.0.1",
    "name": "ScanCodeUpload",
    "group": "excel导入导出",
    "description": "<p>扫码获取32位码录入数据库</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "singlebrand_name",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "code_front",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "code_behind",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    案件编号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n        \"input_caseid\":\"202004120845\",\n        \"singlebrand_name\":\"长白山(海蓝)\",\n        \"code_front\":\"zscd124574584875\",\n        \"code_behind\":\"\",\n        \"user_id\":1\n    }",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\",\n    \"singlebrand_name\":\"长白山(海蓝)\",\n    \"code_front\":\"zscd124574584875\",\n    \"code_behind\":\"1458745214851256\",\n    \"user_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n        \"sys_status\": \"FAIL\",\n        \"data\": null,\n        \"message\": \"请输入完整的32位喷码\"\n    }",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": null,\n     \"message\": \"喷码录入成功\"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/ScanCodeUpload"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/case/getAllExcelInandOutInfo",
    "title": "通过get获取excel导入表中的全部信息",
    "version": "0.0.1",
    "name": "getAllExcelInandOutInfo",
    "group": "excel导入导出",
    "description": "<p>直接获取所有零售户信息,未使用分页</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getAllExcelInandOutInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getAllExcelInandOutInfobycaseid",
    "title": "通过案件编号获取excel导入表中的详细信息",
    "version": "0.0.1",
    "name": "getAllExcelInandOutInfobycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号获取excel导入表中的详细信息,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004132145\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getAllExcelInandOutInfobycaseid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getAllExcelInandOutInfobycaseidBypagi",
    "title": "通过案件编号获取excel导入表中符合该案件编号的详细信息__带分页",
    "version": "0.0.1",
    "name": "getAllExcelInandOutInfobycaseidBypagi",
    "group": "excel导入导出",
    "description": "<p>通过案件编号获取excel导入表中符合该案件编号的详细信息__带分页,使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004132145\",\n     \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 1044,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"thisresultStr123\",\n                \"code_behind\": \"thisresultStr234\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1045,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1046,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1047,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1048,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1049,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1050,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            },\n            {\n                \"id\": 1051,\n                \"input_caseid\": \"202004132145\",\n                \"singlebrand_id\": \"2af3e4119e1b466e810de5365d5bcf3e\",\n                \"singlebrand_name\": \"长白山(海蓝)\",\n                \"code_front\": \"\",\n                \"code_behind\": \"\",\n                \"count\": \"1.00\"\n            }\n        ],\n        \"count\": 96\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getAllExcelInandOutInfobycaseidBypagi"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getAllsinglenamebycaseid",
    "title": "通过案件编号获取该案件编号下全部品规",
    "version": "0.0.1",
    "name": "getAllsinglenamebycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号获取该案件编号下全部品规,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"singlebrand_name\": \"长白山(海蓝)\"\n            },\n            {\n                \"singlebrand_name\": \"长白山(777)\"\n            }\n        ],\n        \"count\": 2\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getAllsinglenamebycaseid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getAllsinglenamecountbycaseid",
    "title": "通过案件编号和品规名称获取该案件编号下该品规的全部数量",
    "version": "0.0.1",
    "name": "getAllsinglenamecountbycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号和品规名称获取该案件编号下该品规的全部数量,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "singlebrand_name",
            "description": "<p>(必须)    品规</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\",\n    \"singlebrand_name\":\"长白山(海蓝)\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": 105,\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getAllsinglenamecountbycaseid"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/case/getUncomplishCaseidInfo",
    "title": "通过get获取excel表中未完成的案件编号",
    "version": "0.0.1",
    "name": "getUncomplishCaseidInfo",
    "group": "excel导入导出",
    "description": "<p>通过get获取excel表中未完成的案件编号,未使用分页</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getUncomplishCaseidInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getUncomplishsinglenamebycaseid",
    "title": "通过案件编号获取该案件编号下未完成的品规",
    "version": "0.0.1",
    "name": "getUncomplishsinglenamebycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号获取该案件编号下未完成的品规,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"singlebrand_name\": \"长白山(海蓝)\"\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getUncomplishsinglenamebycaseid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getUncomplishsinglenamecountbycaseid",
    "title": "通过案件编号和品规名称获取该案件编号下该品规的未完成数量",
    "version": "0.0.1",
    "name": "getUncomplishsinglenamecountbycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号和品规名称获取该案件编号下该品规的未完成数量,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "singlebrand_name",
            "description": "<p>(必须)    品规</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\",\n    \"singlebrand_name\":\"长白山(海蓝)\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": 103,\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getUncomplishsinglenamecountbycaseid"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/case/getcomplishCaseidInfo",
    "title": "通过get获取excel表中已经完成的案件编号",
    "version": "0.0.1",
    "name": "getcomplishCaseidInfo",
    "group": "excel导入导出",
    "description": "<p>通过get获取excel表中已经完成的案件编号,未使用分页</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcomplishCaseidInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getcomplishsinglenamebycaseid",
    "title": "通过案件编号获取该案件编号下已经完成的品规",
    "version": "0.0.1",
    "name": "getcomplishsinglenamebycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号获取该案件编号下已经完成的品规,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"singlebrand_name\": \"长白山(777)\"\n             }\n         ],\n         \"count\": 1\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcomplishsinglenamebycaseid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/case/getcomplishsinglenamecountbycaseid",
    "title": "通过案件编号和品规名称获取该案件编号下该品规的已经完成数量",
    "version": "0.0.1",
    "name": "getcomplishsinglenamecountbycaseid",
    "group": "excel导入导出",
    "description": "<p>通过案件编号和品规名称获取该案件编号下该品规的已经完成数量,未使用分页</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "input_caseid",
            "description": "<p>(必须)    案件编号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "singlebrand_name",
            "description": "<p>(必须)    品规</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"input_caseid\":\"202004120845\",\n    \"singlebrand_name\":\"长白山(海蓝)\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": 2,\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/case.py",
    "groupTitle": "excel导入导出",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/case/getcomplishsinglenamecountbycaseid"
      }
    ]
  },
  {
    "type": "post",
    "url": "/api/forecast/getWarningParams",
    "title": "查询预警等级参数",
    "version": "0.0.1",
    "name": "Warning_params",
    "group": "forecast",
    "description": "<p>查询预警等级参数</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "enum",
            "optional": false,
            "field": "model_warning_params",
            "description": "<p>(必须)    查询模型(Rule or BP)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n      \"model_warning_params\":\"Rule\"\n}",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n      \"model_warning_params\":\"BP\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"param1\": \"0.30\",\n        \"param2\": \"0.60\",\n        \"param3\": \"0.80\"\n    },\n   \"message\": \"预警等级参数查询成功\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n    \"data\": {\n         \"param1\": \"0.60\",\n         \"param2\": null,\n        \"param3\": null\n    },\n   \"message\": \"预警等级参数查询成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/forecast.py",
    "groupTitle": "forecast",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000//api/forecast/getWarningParams"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/forecast/getForecastResultByModel",
    "title": "查询规则模型或者综合模型预测结果",
    "version": "0.0.1",
    "name": "getForecastResultByModel",
    "group": "forecast",
    "description": "<p>查询规则模型或者综合模型预测结果</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "enum",
            "optional": false,
            "field": "forecast_model",
            "description": "<p>(必须)    预测模型</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n         \"forecast_model\":\"Rule\" (or \"Comprehensive\"(综合模型）)\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"\"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"TOP\": [\n           {\n               \"id\": 7,\n               \"store_name\": \"金华市婺城区开怀副食品商店\",\n              \"name\": \"郑开怀\",\n              \"phone\": \"13065955982\",\n              \"administrative\": {\n                    \"BENJI\": \"本级\"\n              },\n              \"longitude\": \"119.66\",\n             \"latitude\": \"29.09\",\n             \"address\": \"金华市婺城区中村路76号\",\n             \"forecast_date\": \"2020-03-23\",\n             \"result\": \"0.89\"\n           },\n           {\n              \"id\": 6,\n              \"store_name\": \"金华市婺城区徐设波副食便利店\",\n              \"name\": \"徐设波\",\n              \"phone\": \"13735714658\",\n              \"administrative\": {\n                 \"BENJI\": \"本级\"\n              },\n              \"longitude\": \"119.66\",\n              \"latitude\": \"29.10\",\n              \"address\": \"金华市婺城区亚峰路113号\",\n              \"forecast_date\": \"2020-03-23\",\n              \"result\": \"0.85\"\n           },\n           {\n             \"id\": 2,\n             ...同上\n           },\n           {\n             \"id\": 1,\n              ...同上\n           }\n        ],\n        \"MIDDLE\": [\n          {\n             \"id\": 10,\n             \"store_name\": \"金华市婺城区王文娟副食便利店\",\n             \"name\": \"王文娟\",\n             \"phone\": \"13357056183\",\n             \"administrative\": {\n                  \"BENJI\": \"本级\"\n            },\n             \"longitude\": \"119.66\",\n             \"latitude\": \"29.09\",\n             \"address\": \"金华市婺城区江南街道金钱寺社区明星路32号\",\n             \"forecast_date\": \"2020-03-23\",\n             \"result\": \"0.75\"\n          },\n          {\n             \"id\": 9,\n             ...同上\n          },\n          {\n            \"id\": 8,\n            ...同上\n          },\n          {\n           \"id\": 3,\n            ...同上\n          }\n       ],\n      \"LOW\": [\n         {\n           \"id\": 11,\n           \"store_name\": \"金华市婺城区金松烟酒店\",\n           \"name\": \"钱金松\",\n           \"phone\": \"15925758598\",\n           \"administrative\": {\n               \"BENJI\": \"本级\"\n           },\n            \"longitude\": \"119.65\",\n            \"latitude\": \"29.09\",\n            \"address\": \"金华市婺城区江南街道中村路127弄35号\",\n            \"forecast_date\": \"2020-03-23\",\n            \"result\": \"0.45\"\n         },\n         {\n            \"id\": 4,\n              ...同上\n         }\n      ]\n    },\n   \"message\": \"规则模型预测结果查询成功\"\n   综合模型预测结果同上，不再赘述\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/forecast.py",
    "groupTitle": "forecast",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/forecast/getForecastResultByModel"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/forecast/modifyWarningParams",
    "title": "修改预警等级参数",
    "version": "0.0.1",
    "name": "modify_warning_params",
    "group": "forecast",
    "description": "<p>修改预警等级参数</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "enum",
            "optional": false,
            "field": "model_warning_params",
            "description": "<p>(必须)    模型(Rule or BP)</p>"
          },
          {
            "group": "Parameter",
            "type": "number",
            "optional": false,
            "field": "param1",
            "description": "<p>(可选)    预警参数1(必须两位精度，两位小数，大于0且小于1)</p>"
          },
          {
            "group": "Parameter",
            "type": "number",
            "optional": false,
            "field": "param2",
            "description": "<p>(可选)    预警参数2(必须两位精度，两位小数，大于0且小于1)</p>"
          },
          {
            "group": "Parameter",
            "type": "number",
            "optional": false,
            "field": "param3",
            "description": "<p>(可选)    预警参数3(必须两位精度，两位小数，大于0且小于1)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n        \"model_warning_params\":\"RULE\",\n        \"param1\":\"0.30\",\n        \"param2\":\"0.60\",\n        \"param3\":\"0.80\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"模型预警参数修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/forecast.py",
    "groupTitle": "forecast",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/forecast/modifyWarningParams"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/rule/delRule",
    "title": "停用规则",
    "version": "0.0.1",
    "name": "delete_rule",
    "group": "rule",
    "description": "<p>停用规则</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "rule_name",
            "description": "<p>(必须)    规则名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "rule_id",
            "description": "<p>(必须)    规则id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"rule_name\":\"person_nativeplace\",\n    \"rule_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"规则停用成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/rule.py",
    "groupTitle": "rule",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/rule/delRule"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/rule/getHighRiskStore",
    "title": "根据零售户id查询分数构成及预测案由",
    "version": "0.0.1",
    "name": "getHighriskStore",
    "group": "rule",
    "description": "<p>根据零售户id查询分数构成及预测案由</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    经营户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    第一行是零售户id，\n    依次40个规则得分，\n    最后一行为预测案由\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/rule.py",
    "groupTitle": "rule",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/rule/getHighRiskStore"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/rule/modifyRuleInfo",
    "title": "修改预警规则",
    "version": "0.0.1",
    "name": "rule_modify",
    "group": "rule",
    "description": "<p>修改预警规则</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "rule_id",
            "description": "<p>(必须)    规则id</p>"
          },
          {
            "group": "Parameter",
            "type": "tinyint",
            "optional": false,
            "field": "is_delete",
            "description": "<p>(可选)    是否删除</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "rule_name",
            "description": "<p>(可选)    规则名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "parameter1",
            "description": "<p>(可选)    参数一</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "parameter2",
            "description": "<p>(可选)    参数二</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "parameter3",
            "description": "<p>(可选)    参数三</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "parameter4",
            "description": "<p>(可选)    参数四</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "score1",
            "description": "<p>(可选)    分数一</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "score2",
            "description": "<p>(可选)    分数二</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "score3",
            "description": "<p>(可选)    分数三</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "score4",
            "description": "<p>(可选)    分数四</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "describe_rule",
            "description": "<p>(可选)    预警参数描述</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "modifydate",
            "description": "<p>(可选)    修改日期</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"score1\":5,\n    \"rule_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"规则修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/rule.py",
    "groupTitle": "rule",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/rule/modifyRuleInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/rule/staRule",
    "title": "启用规则",
    "version": "0.0.1",
    "name": "start_rule",
    "group": "rule",
    "description": "<p>启用规则</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "rule_name",
            "description": "<p>(必须)    规则名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "rule_id",
            "description": "<p>(必须)    规则id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"rule_name\":\"person_nativeplace\",\n    \"rule_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"规则启用成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/rule.py",
    "groupTitle": "rule",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/rule/staRule"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/addDepartment",
    "title": "添加稽查所",
    "version": "0.0.1",
    "name": "add_depart",
    "group": "station",
    "description": "<p>添加稽查所</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "depart_name",
            "description": "<p>(必须)    稽查所名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    专卖局id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"depart_name\":\"锦衣卫\",\n    \"station_id\":2\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"稽查所添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": \"锦衣卫\",\n    \"message\": \"该稽查所已被添加\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/addDepartment"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/addStation",
    "title": "添加专卖局",
    "version": "0.0.1",
    "name": "add_station",
    "group": "station",
    "description": "<p>添加专卖局</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "station_name",
            "description": "<p>(必须)    专卖局名称</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_name\":\"一处\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"专卖局添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": \"一处\",\n    \"message\": \"该专卖局已被添加\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/addStation"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/delDepartment",
    "title": "删除稽查所",
    "version": "0.0.1",
    "name": "del_depart",
    "group": "station",
    "description": "<p>删除稽查所</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "depart_name",
            "description": "<p>(必须)    稽查所名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须)    稽查所id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"depart_name\":\"锦衣卫\",\n    \"department_id\":4\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"稽查所删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/delDepartment"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/delStation",
    "title": "删除专卖局",
    "version": "0.0.1",
    "name": "delete_station",
    "group": "station",
    "description": "<p>删除专卖局</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "station_name",
            "description": "<p>(必须)    专卖局名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    专卖局id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_name\":\"二处\",\n    \"station_id\":11\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"专卖局删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/delStation"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/station/modifyDepartInfo",
    "title": "修改稽查所",
    "version": "0.0.1",
    "name": "depart_modify",
    "group": "station",
    "description": "<p>修改稽查所</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须)    稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "depart_name",
            "description": "<p>(可选)    稽查所名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(可选)    专卖局id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"department_id\":3,\n    \"depart_name\":\"清风港稽查所\",\n    \"station_id\":11\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"稽查所信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/modifyDepartInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/getAllUserByStationid",
    "title": "根据局id获取所辖稽查人员",
    "version": "0.0.1",
    "name": "getAllUserByStationid",
    "group": "station",
    "description": "<p>根据局id获取所辖稽查人员,此接口使用了分页功能，page参数通过表单提交,per_page参数指定一页有多获取多少数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"role_id\":2,\n    \"station_id\":1,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 4,\n                \"account\": \"40040004000\",\n                \"password\": \"123456\",\n                \"role_id\": 3,\n                \"department_id\": 1,\n                \"station_id\": 1,\n                \"user_name\": \"胡适\"\n            },\n            {\n                \"id\": 3,\n                \"account\": \"30030003000\",\n                \"password\": \"123456\",\n                \"role_id\": 2,\n                \"department_id\": 2,\n                \"station_id\": 1,\n                \"user_name\": \"鲁迅\"\n            },\n            {\n                \"id\": 2,\n                \"account\": \"20020002000\",\n                \"password\": \"123456\",\n                \"role_id\": 1,\n                \"department_id\": 1,\n                \"station_id\": 1,\n                \"user_name\": \"老大\"\n            },\n            {\n                \"id\": 1,\n                \"account\": \"10010001000\",\n                \"password\": \"123456\",\n                \"role_id\": 4,\n                \"department_id\": 1,\n                \"station_id\": 1,\n                \"user_name\": \"杨秋月\"\n            }\n        ],\n        \"count\": 4\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": null,\n    \"message\": \"无查询结果\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getAllUserByStationid"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/station/getDepartnameBydepartid",
    "title": "通过稽查所id获取稽查所名字",
    "version": "0.0.1",
    "name": "getDepartnameBydepartid",
    "group": "station",
    "description": "<p>通过稽查所id获取稽查所名字</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须)    稽查所id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"department_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": [\n         {\n             \"depart_name\": \"二所一片\",\n             \"station_id\": 1,\n             \"station_name\": \"金华市专卖局\"\n         }\n     ],\n     \"message\": \"成功\"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getDepartnameBydepartid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/getStationInfoByStationname",
    "title": "通过专卖局名称获取专卖局详细信息--分页—--杨",
    "version": "0.0.1",
    "name": "getStationInfoByStationname",
    "group": "station",
    "description": "<p>通过专卖局名称获取专卖局详细信息--分页—--杨</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "station_name",
            "description": "<p>(必须)    专卖局名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_name\":\"金华市专卖局\",\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            }\n        ],\n        \"count\": 1\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getStationInfoByStationname"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/station/getAllDepartByStation",
    "title": "根据局获取所辖稽查所",
    "version": "0.0.1",
    "name": "get_AllDepart_byStation",
    "group": "station",
    "description": "<p>根据局id获取所辖稽查所,此接口使用了分页功能，page参数通过表单提交</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": {\n         \"data\": [\n             {\n                 \"id\": 1,\n                 \"depart_name\": \"二所一片\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 2,\n                 \"depart_name\": \"二所二片\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 3,\n                 \"depart_name\": \"二所三片\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 4,\n                 \"depart_name\": \"二所四片\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 5,\n                 \"depart_name\": \"二所五片1\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 6,\n                 \"depart_name\": \"二所六片\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 7,\n                 \"depart_name\": \"二所七片\",\n                 \"station_name\": \"金华市专卖局\"\n             },\n             {\n                 \"id\": 8,\n                 \"depart_name\": \"二所八片\",\n                 \"station_name\": \"金华市专卖局\"\n             }\n         ],\n         \"count\": 14\n     },\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": null,\n    \"message\": \"无查询结果\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getAllDepartByStation"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/station/getAllByRole",
    "title": "根据角色id和和局id或者稽查所id获取所辖稽查所和稽查人员",
    "version": "0.0.1",
    "name": "get_AllInfo_byAdminid",
    "group": "station",
    "description": "<p>这个接口是提供给局长和稽查所所长使用，接受角色2和3的用户，提供角色id和响应的局id或者所id，可以获取辖区的稽查所和稽查人员,此接口使用了分页功能，page参数通过表单提交</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id，仅接受2 和 3</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(可选)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(可选)    稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":1,\n    \"role_id\":2,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n    \"department_id\":1,\n    \"role_id\":3,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 9,\n            \"depart_name\": \"二所九片\"\n        },\n        {\n            \"id\": 8,\n            \"depart_name\": \"二所八片\"\n        },\n        {\n            \"id\": 7,\n            \"depart_name\": \"二所七片\"\n        },\n        {\n            \"id\": 6,\n            \"depart_name\": \"二所六片\"\n        },\n        {\n            \"id\": 5,\n            \"depart_name\": \"二所五片\"\n        },\n        {\n            \"id\": 4,\n            \"depart_name\": \"二所四片\"\n        },\n        {\n            \"id\": 3,\n            \"depart_name\": \"二所三片\"\n        },\n        {\n            \"id\": 2,\n            \"depart_name\": \"二所二片\"\n        },\n        {\n            \"id\": 1,\n            \"depart_name\": \"二所一片\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 4,\n            \"user_name\": \"胡适\"\n        },\n        {\n            \"id\": 2,\n            \"user_name\": \"老大\"\n        },\n        {\n            \"id\": 1,\n            \"user_name\": \"杨秋月\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": null,\n    \"message\": \"无查询结果\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getAllByRole"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/station/getAllDepart",
    "title": "直接获取所有稽查所",
    "version": "0.0.1",
    "name": "get_All_Depart",
    "group": "station",
    "description": "<p>直接获取所有稽查所，此处使用了分页功能，因为是get方法，所以page参数指定访问第几页，per_page参数指定一页多少条</p>",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n示例:http://39.96.52.170:5000/api/station/getAllDepart?page=2&per_page=8  可以获取第二页的内容,数据库中数据不够多，还没有第二页\n    }",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " {\n    \"sys_status\": \"SUCCESS\",\n    \"data\": {\n        \"data\": [\n            {\n                \"id\": 9,\n                \"depart_name\": \"二所九片\",\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            },\n            {\n                \"id\": 10,\n                \"depart_name\": \"二所十片\",\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            },\n            {\n                \"id\": 11,\n                \"depart_name\": \"二所十一片\",\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            },\n            {\n                \"id\": 12,\n                \"depart_name\": \"二所十二片\",\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            },\n            {\n                \"id\": 14,\n                \"depart_name\": \"二所十三片\",\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            },\n            {\n                \"id\": 15,\n                \"depart_name\": \"二所十四片\",\n                \"station_id\": 1,\n                \"station_name\": \"金华市专卖局\"\n            },\n            {\n                \"id\": 19,\n                \"depart_name\": \"一所\",\n                \"station_id\": 8,\n                \"station_name\": \"永康市专卖局\"\n            },\n            {\n                \"id\": 20,\n                \"depart_name\": \"二所\",\n                \"station_id\": 8,\n                \"station_name\": \"永康市专卖局\"\n            }\n        ],\n        \"count\": 16\n    },\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getAllDepart"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/station/getAllStation",
    "title": "直接获取所有专卖局",
    "version": "0.0.1",
    "name": "get_All_Station",
    "group": "station",
    "description": "<p>直接获取所有专卖局,此处使用了分页功能，因为是get方法，所以page参数指定访问第几页，per_page参数指定一页多少条</p>",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n示例:http://39.96.52.170:5000/api/station/getAllStation?page=2&per_page=8  可以获取第二页的内容,数据库中数据不够多，还没有第二页\n    }",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n                {\n                    \"id\": 1,\n                    \"station_name\": \"金华专卖局\"\n                }\n            ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getAllStation"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/station/getAllUser",
    "title": "直接获取所有稽查人员",
    "version": "0.0.1",
    "name": "get_All_User",
    "group": "station",
    "description": "<p>直接获取所有稽查人员，此处使用了分页功能，因为是get方法，所以page参数指定访问第几页，per_page参数指定一页多少条</p>",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n示例:http://39.96.52.170:5000/api/station/getAllUser?page=2&per_page=8  可以获取第二页的内容,数据库中数据不够多，还没有第二页\n    }",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 2,\n            \"user_name\": \"老大\"\n        },\n        {\n            \"id\": 1,\n            \"user_name\": \"杨秋月\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/getAllUser"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/station/modifyStationInfo",
    "title": "修改专卖局",
    "version": "0.0.1",
    "name": "station_modify",
    "group": "station",
    "description": "<p>修改专卖局</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "station_id",
            "description": "<p>(必须)    专卖局id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "station_name",
            "description": "<p>(可选)    专卖局名称</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"station_id\":11,\n    \"station_name\":\"二处\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"专卖局信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/station.py",
    "groupTitle": "station",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/station/modifyStationInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/store/addPersonInfo",
    "title": "添加法人信息",
    "version": "0.0.1",
    "name": "addPersonInfo",
    "group": "store",
    "description": "<p>添加法人信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>(必须)    法人姓名</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": "<p>(必须)    性别</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id_card",
            "description": "<p>(必须)    零售户法人信息id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id_address",
            "description": "<p>(可选)    身份证住址</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "birthday",
            "description": "<p>(可选)    出生日期</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "nation",
            "description": "<p>(可选)    民族</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "census_register",
            "description": "<p>(可选)    籍贯</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>(可选)    联系电话</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>(可选)    地址</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"name\":\"李三黑\",\n    \"sex\":\"True\",\n    \"id_card\":\"341282199503026057\",\n    \"id_address\":\"金华市婺城区浙江师范大学\",\n    \"birthday\":\"1995-08-08\",\n    \"nation\":\"汉族\",\n    \"census_register\":\"金华市婺城区\",\n    \"phone\":\"18225879332\",\n    \"address\":\"金华市婺城区义乌街151号\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"法人添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n     \"sys_status\": \"FAIL\",\n     \"data\": \"李三黑\",\n     \"message\": \"该法人已被添加\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/addPersonInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/store/addStore",
    "title": "添加店铺",
    "version": "0.0.1",
    "name": "add_store",
    "group": "store",
    "description": "<p>添加店铺</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "store_name",
            "description": "<p>(必须)    店铺名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须，稽查所表中必须先有数据)    所属稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "person_id",
            "description": "<p>(必须，法人信息表中必须先有数据)    零售户法人信息id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "picture",
            "description": "<p>(可选)    店铺俯视图</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "business_number",
            "description": "<p>(必须)    烟草经营许可证号</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_bigillegal",
            "description": "<p>(可选)    是否为违法大户</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "business_start",
            "description": "<p>(可选)    烟草经营许可证有效期始</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "business_termi",
            "description": "<p>(可选)    烟草经营许可证有效期止</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "longitude",
            "description": "<p>(必须)    地址经度</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "latitude",
            "description": "<p>(必须)    地址纬度</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>(可选)    经营地址</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "state",
            "description": "<p>(可选)    经营状态</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "store_category",
            "description": "<p>(可选)    零售户合理定量类别</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_chain",
            "description": "<p>(可选)    是否连锁</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_suspension",
            "description": "<p>(可选)    是否暂停货源</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "business_format",
            "description": "<p>(可选)    经营业态</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "administrative",
            "description": "<p>(可选)    行政区划分</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "market_type",
            "description": "<p>(可选)    市场类型</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>(可选)    主呼电话</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "settlement_account",
            "description": "<p>(可选)    电子结算账号</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "circle",
            "description": "<p>(可选)   是否敏感商圈</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_downgrade",
            "description": "<p>(可选)    是否有降级降档情况</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_1",
            "description": "<p>(可选)    车辆牌照1</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_2",
            "description": "<p>(可选)    车辆牌照2</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_3",
            "description": "<p>(可选)    车辆牌照3</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_photo1",
            "description": "<p>(可选)    车辆牌照图1</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_photo2",
            "description": "<p>(可选)    车辆牌照图2</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_photo3",
            "description": "<p>(可选)    车辆牌照图3</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "operators1",
            "description": "<p>(可选)    日常经营人1</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "license_ship1",
            "description": "<p>(可选)    与持证人关系1</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "operators2",
            "description": "<p>(可选)    日常经营人2</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "license_ship2",
            "description": "<p>(可选)    与持证人关系2</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "operators3",
            "description": "<p>(可选)    日常经营人3</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "license_ship3",
            "description": "<p>(可选)    与持证人关系3</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "special_category",
            "description": "<p>(可选)    特殊群体类别</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_name\":\"金华市龙门客栈食品便利店\",\n    \"department_id\":2,\n    \"person_id\":1522,\n    \"picture\":\"18125412365\",\n    \"business_number\":\"3307274582488\",\n    \"is_bigillegal\":\"True\",\n    \"business_start\":\"2018-08-08\",\n    \"business_termi\":\"2020-10-10\",\n    \"longitude\":\"119.526345\",\n    \"latitude\":\"29.451287\",\n    \"address\":\"金华市婺城区义乌街151号\",\n    \"state\":\"NARMAL\",\n    \"store_category\":\"B3\",\n    \"is_chain\":\"True\",\n    \"is_suspension\":\"False\",\n    \"business_format\":\"TOP\",\n    \"administrative\":\"BENJI\",\n    \"market_type\":\"URBAN\",\n    \"phone\":\"13665884899\",\n    \"settlement_account\":\"54125412578545\",\n    \"circle\":\"True\",\n    \"is_downgrade\":\"True\",\n    \"car_1\":\"ldskggelgk\",\n    \"car_2\":\"kdsjkgjdkj\",\n    \"car_3\":\"dskgjkjg\",\n    \"car_photo1\":\"dksgkjg\",\n    \"car_photo2\":\"djgdjkgj\",\n    \"car_photo3\":\"dksjgkjjk\",\n    \"operators1\":\"李翠花\",\n    \"license_ship1\":\"EMPLOY\",\n    \"operators2\":\"linda\",\n    \"license_ship2\":\"RELATION\",\n    \"operators3\":\"诸葛亮\",\n    \"license_ship3\":\"OTHER\",\n    \"special_category\":\"VIOLENCE\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"店铺添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"sys_status\": \"FAIL\",\n    \"data\": \"金华市龙门客栈食品便利店\",\n    \"message\": \"该零售户已被添加\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/addStore"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/delPersoninfo",
    "title": "删除法人信息",
    "version": "0.0.1",
    "name": "delPersoninfo",
    "group": "store",
    "description": "<p>删除法人信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>(必须)    法人姓名</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "person_id",
            "description": "<p>(必须)    法人id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"name\":\"李旋风\",\n    \"person_id\":1524\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"法人删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/delPersoninfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/delStore",
    "title": "删除店铺",
    "version": "0.0.1",
    "name": "delete_store",
    "group": "store",
    "description": "<p>删除店铺</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "store_name",
            "description": "<p>(必须)    店铺名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    店铺id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_name\":\"金华市永亮烟酒商行\",\n    \"store_id\":1533\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"零售户删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/delStore"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/store/getAllPersonInfo",
    "title": "直接获取所有法人信息",
    "version": "0.0.1",
    "name": "getAllPersonInfo",
    "group": "store",
    "description": "<p>直接获取所有法人信息,此处使用了分页功能，因为是get方法，所以page参数通过访问地址访问，per_page参数指定每页显示多少内容</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n   示例:http://39.96.52.170:5000/api/store/getAllPersonInfo?page=2&per_page=8  可以获取第二页的8条内容\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllPersonInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getAllPersonInfoByname",
    "title": "通过法人姓名查询法人",
    "version": "0.0.1",
    "name": "getAllPersonInfoByname",
    "group": "store",
    "description": "<p>通过法人姓名查询法人</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>(必须)    法人姓名</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"name\":\"李三黑\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1524,\n            \"name\": \"李三黑\",\n            \"sex\": 0,\n            \"id_card\": \"330723198807114128\",\n            \"id_address\": \"金华市婺城区浙江师范大学\",\n            \"birthday\": \"1995-08-08\",\n            \"nation\": \"汉族\",\n            \"census_register\": \"金华市婺城区\",\n            \"phone\": \"18225879332\",\n            \"address\": \"金华市婺城区义乌街151号\"\n        },\n        {\n            \"id\": 1523,\n            \"name\": \"李三黑\",\n            \"sex\": 0,\n            \"id_card\": \"341542499567851245\",\n            \"id_address\": \"金华市婺城区浙江师范大学\",\n            \"birthday\": \"1995-08-08\",\n            \"nation\": \"汉族\",\n            \"census_register\": \"金华市婺城区\",\n            \"phone\": \"18225879332\",\n            \"address\": \"金华市婺城区义乌街151号\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllPersonInfoByname"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/store/getAllStoreInfo",
    "title": "直接获取所有零售户信息",
    "version": "0.0.1",
    "name": "getAllStoreInfo",
    "group": "store",
    "description": "<p>直接获取所有零售户信息,此处使用了分页功能，因为是get方法，所以page参数通过访问地址访问，通过per_page指定每页显示多少条数据</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n   示例:http://39.96.52.170:5000/api/store/getAllStoreInfo?page=2&per_page=8  可以获取第二页的8条内容\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllStoreInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getAllStoreInfoByDepartid",
    "title": "查询某个稽查所下所有零售户",
    "version": "0.0.1",
    "name": "getAllStoreInfoByDepartid",
    "group": "store",
    "description": "<p>查询某个稽查所下所有零售户,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须)    稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"department_id\":1,\n    \"page\":2,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    省略\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllStoreInfoByDepartid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getAllStoreInfoByStorename",
    "title": "通过零售户名查询零售户",
    "version": "0.0.1",
    "name": "getAllStoreInfoByStorename",
    "group": "store",
    "description": "<p>通过零售户名查询零售户</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "store_name",
            "description": "<p>(必须)    零售户名称</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_name\":\"金华市婺城区文丽烟店\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " {\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"store_name\": \"金华市婺城区文丽烟店\",\n            \"id\": 3,\n            \"department_id\": 2,\n            \"depart_name\": \"二所二片\",\n            \"person_id\": 3,\n            \"name\": \"高文丽\",\n            \"picture\": null,\n            \"business_number\": \"330701203202\",\n            \"is_bigillegal\": false,\n            \"business_start\": \"2016-09-12\",\n            \"business_termi\": \"2021-09-01\",\n            \"longitude\": \"119.66\",\n            \"latitude\": \"29.08\",\n            \"address\": \"金华市婺城区宾虹路439弄2幢\",\n            \"state\": {\n                \"NARMAL\": \"正常营业\"\n            },\n            \"store_category\": \"D4\",\n            \"is_chain\": false,\n            \"is_suspension\": false,\n            \"business_format\": null,\n            \"administrative\": null,\n            \"market_type\": null,\n            \"phone\": \"15355894148\",\n            \"settlement_account\": null,\n            \"circle\": null,\n            \"is_downgrade\": null,\n            \"car_1\": null,\n            \"car_2\": null,\n            \"car_3\": null,\n            \"car_photo1\": null,\n            \"car_photo2\": null,\n            \"car_photo3\": null,\n            \"operators1\": null,\n            \"license_ship1\": null,\n            \"operators2\": null,\n            \"license_ship2\": null,\n            \"operators3\": null,\n            \"license_ship3\": null,\n            \"special_category\": null\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllStoreInfoByStorename"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getAllStoreInfoByStorenameAndPersonname",
    "title": "通过零售户名或者法人名称查询零售户",
    "version": "0.0.1",
    "name": "getAllStoreInfoByStorenameAndPersonname",
    "group": "store",
    "description": "<p>通过零售户名或者法人名称查询零售户</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>(必须)    零售户名称或者法人名称</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"name\":\"金华市婺城区文丽烟店\"\n}",
          "type": "json"
        },
        {
          "title": "Request-Example:",
          "content": "{\n    \"name\":\"沈美香\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"store_name\": \"金华市婺城区文丽烟店\",\n            \"id\": 3,\n            \"department_id\": 2,\n            \"depart_name\": \"二所二片\",\n            \"person_id\": 3,\n            \"name\": \"高文丽\",\n            \"picture\": null,\n            \"business_number\": \"330701203202\",\n            \"is_bigillegal\": false,\n            \"business_start\": \"2016-09-12\",\n            \"business_termi\": \"2021-09-01\",\n            \"longitude\": \"119.66\",\n            \"latitude\": \"29.08\",\n            \"address\": \"金华市婺城区宾虹路439弄2幢\",\n            \"state\": {\n                \"NARMAL\": \"正常营业\"\n            },\n            \"store_category\": \"D4\",\n            \"is_chain\": false,\n            \"is_suspension\": false,\n            \"business_format\": null,\n            \"administrative\": null,\n            \"market_type\": null,\n            \"phone\": \"15355894148\",\n            \"settlement_account\": null,\n            \"circle\": null,\n            \"is_downgrade\": null,\n            \"car_1\": null,\n            \"car_2\": null,\n            \"car_3\": null,\n            \"car_photo1\": null,\n            \"car_photo2\": null,\n            \"car_photo3\": null,\n            \"operators1\": null,\n            \"license_ship1\": null,\n            \"operators2\": null,\n            \"license_ship2\": null,\n            \"operators3\": null,\n            \"license_ship3\": null,\n            \"special_category\": null\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "{\n            \"sys_status\": \"SUCCESS\",\n            \"data\": [\n                {\n                    \"name\": \"沈美香\",\n                    \"store_name\": \"金华市婺城区沈美香副食店\",\n                    \"id\": 5,\n                    \"department_id\": 2,\n                    \"depart_name\": \"二所二片\",\n                    \"person_id\": 5,\n                    \"picture\": null,\n                    \"business_number\": \"330701103983\",\n                    \"is_bigillegal\": false,\n                    \"business_start\": \"2016-08-31\",\n                    \"business_termi\": \"2021-08-15\",\n                    \"longitude\": \"119.66\",\n                    \"latitude\": \"29.09\",\n                    \"address\": \"金华市婺城区中村社区中南巷10幢3单元102室\",\n                    \"state\": {\n                        \"NARMAL\": \"正常营业\"\n                    },\n                    \"store_category\": \"D7\",\n                    \"is_chain\": false,\n                    \"business_format\": null,\n                    \"administrative\": null,\n                    \"market_type\": null,\n                    \"phone\": \"15325891963\",\n                    \"settlement_account\": null,\n                    \"circle\": null,\n                    \"is_downgrade\": null,\n                    \"car_1\": null,\n                    \"car_2\": null,\n                    \"car_3\": null,\n                    \"car_photo1\": null,\n                    \"car_photo2\": null,\n                    \"car_photo3\": null,\n                    \"operators1\": null,\n                    \"license_ship1\": null,\n                    \"operators2\": null,\n                    \"license_ship2\": null,\n                    \"operators3\": null,\n                    \"license_ship3\": null,\n                    \"special_category\": null\n                }\n            ],\n            \"message\": \" \"\n        }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllStoreInfoByStorenameAndPersonname"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getAllStoreInfodepartbossid",
    "title": "稽查所所长查询本所下所有零售户",
    "version": "0.0.1",
    "name": "getAllStoreInfodepartbossid",
    "group": "store",
    "description": "<p>稽查所所长查询本所下所有零售户,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(必须)    稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"department_id\":1,\n    \"role_id\":3,\n    \"page\":2,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    省略\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getAllStoreInfodepartbossid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getPersonInfoByStoreid",
    "title": "根据店铺id获取法人信息",
    "version": "0.0.1",
    "name": "getPersonInfoByStoreid",
    "group": "store",
    "description": "<p>根据店铺id获取法人信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 5,\n            \"name\": \"沈美香\",\n            \"sex\": 0,\n            \"id_card\": null,\n            \"id_address\": null,\n            \"birthday\": \"1963-08-14\",\n            \"nation\": null,\n            \"census_register\": null,\n            \"phone\": \"15325891963\",\n            \"address\": null\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getPersonInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getPersonInfoByid",
    "title": "通过法人id获取法人详细信息",
    "version": "0.0.1",
    "name": "getPersonInfoByid",
    "group": "store",
    "description": "<p>通过法人id获取法人详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "person_id",
            "description": "<p>(必须)    法人id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"person_id\":1524\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1524,\n            \"name\": \"李三黑\",\n            \"sex\": 0,\n            \"id_card\": \"330723198807114128\",\n            \"id_address\": \"金华市婺城区浙江师范大学\",\n            \"birthday\": \"1995-08-08\",\n            \"nation\": \"汉族\",\n            \"census_register\": \"金华市婺城区\",\n            \"phone\": \"18225879332\",\n            \"address\": \"金华市婺城区义乌街151号\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getPersonInfoByid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getStoreInfoByStoreId",
    "title": "根据零售户id获取分数构成及预测案由",
    "version": "0.0.1",
    "name": "getStoreInfoByStoreId",
    "group": "store",
    "description": "<p>根据零售户id获取分数构成及预测案由</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/rule.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getStoreInfoByStoreId"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getStoreInfoByStoreid",
    "title": "通过零售户id获取零售户详细信息",
    "version": "0.0.1",
    "name": "getStoreInfoByStoreid",
    "group": "store",
    "description": "<p>通过零售户id获取零售户详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"store_name\": \"金华市婺城区沈美香副食店\",\n            \"id\": 5,\n            \"department_id\": 2,\n            \"depart_name\": \"二所二片\",\n            \"person_id\": 5,\n            \"name\": \"沈美香\",\n            \"picture\": null,\n            \"business_number\": \"330701103983\",\n            \"is_bigillegal\": false,\n            \"business_start\": \"2016-08-31\",\n            \"business_termi\": \"2021-08-15\",\n            \"longitude\": \"119.66\",\n            \"latitude\": \"29.09\",\n            \"address\": \"金华市婺城区中村社区中南巷10幢3单元102室\",\n            \"state\": {\n                \"NARMAL\": \"正常营业\"\n            },\n            \"store_category\": \"D7\",\n            \"is_chain\": false,\n            \"is_suspension\": false,\n            \"business_format\": null,\n            \"administrative\": null,\n            \"market_type\": null,\n            \"phone\": \"15325891963\",\n            \"settlement_account\": null,\n            \"circle\": null,\n            \"is_downgrade\": null,\n            \"car_1\": null,\n            \"car_2\": null,\n            \"car_3\": null,\n            \"car_photo1\": null,\n            \"car_photo2\": null,\n            \"car_photo3\": null,\n            \"operators1\": null,\n            \"license_ship1\": null,\n            \"operators2\": null,\n            \"license_ship2\": null,\n            \"operators3\": null,\n            \"license_ship3\": null,\n            \"special_category\": null\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getStoreInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/store/getStoreInfoBypersonid",
    "title": "根据法人id获取店铺信息",
    "version": "0.0.1",
    "name": "getStoreInfoBypersonid",
    "group": "store",
    "description": "<p>根据法人id获取店铺信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "person_id",
            "description": "<p>(必须)    法人id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"person_id\":5\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"store_name\": \"金华市婺城区沈美香副食店\",\n            \"id\": 5,\n            \"department_id\": 2,\n            \"depart_name\": \"二所二片\",\n            \"person_id\": 5,\n            \"name\": \"沈美香\",\n            \"picture\": null,\n            \"business_number\": \"330701103983\",\n            \"is_bigillegal\": false,\n            \"business_start\": \"2016-08-31\",\n            \"business_termi\": \"2021-08-15\",\n            \"longitude\": \"119.66\",\n            \"latitude\": \"29.09\",\n            \"address\": \"金华市婺城区中村社区中南巷10幢3单元102室\",\n            \"state\": {\n                \"NARMAL\": \"正常营业\"\n            },\n            \"store_category\": \"D7\",\n            \"is_chain\": false,\n            \"is_suspension\": false,\n            \"business_format\": null,\n            \"administrative\": null,\n            \"market_type\": null,\n            \"phone\": \"15325891963\",\n            \"settlement_account\": null,\n            \"circle\": null,\n            \"is_downgrade\": null,\n            \"car_1\": null,\n            \"car_2\": null,\n            \"car_3\": null,\n            \"car_photo1\": null,\n            \"car_photo2\": null,\n            \"car_photo3\": null,\n            \"operators1\": null,\n            \"license_ship1\": null,\n            \"operators2\": null,\n            \"license_ship2\": null,\n            \"operators3\": null,\n            \"license_ship3\": null,\n            \"special_category\": null\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/getStoreInfoBypersonid"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/store/modifyPersonInfo",
    "title": "修改法人信息",
    "version": "0.0.1",
    "name": "modifyPersonInfo",
    "group": "store",
    "description": "<p>修改法人信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "person_id",
            "description": "<p>(必须)    法人id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>(可选)    法人姓名</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": "<p>(可选)    性别</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id_card",
            "description": "<p>(可选)    零售户法人信息id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id_address",
            "description": "<p>(可选)    身份证住址</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "birthday",
            "description": "<p>(可选)    出生日期</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "nation",
            "description": "<p>(可选)    民族</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "census_register",
            "description": "<p>(可选)    籍贯</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>(可选)    联系电话</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>(可选)    地址</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"person_id\":1524,\n    \"name\":\"李旋风\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"法人信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/modifyPersonInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/store/modifyStoreInfo",
    "title": "修改店铺信息",
    "version": "0.0.1",
    "name": "store_modify",
    "group": "store",
    "description": "<p>修改店铺信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    店铺id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "store_name",
            "description": "<p>(可选)    店铺名称</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "department_id",
            "description": "<p>(可选)    所属稽查所id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "person_id",
            "description": "<p>(可选)    零售户法人信息id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "picture",
            "description": "<p>(可选)    店铺俯视图</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "business_number",
            "description": "<p>(可选)    烟草经营许可证号</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_bigillegal",
            "description": "<p>(可选)    是否为违法大户</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "business_start",
            "description": "<p>(可选)    烟草经营许可证有效期始</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "business_termi",
            "description": "<p>(可选)    烟草经营许可证有效期止</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "longitude",
            "description": "<p>(可选)    地址经度</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "latitude",
            "description": "<p>(可选)    地址纬度</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>(可选)    经营地址</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "state",
            "description": "<p>(可选)    经营状态</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "store_category",
            "description": "<p>(可选)    零售户合理定量类别</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_chain",
            "description": "<p>(可选)    是否连锁</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_suspension",
            "description": "<p>(可选)    是否暂停货源</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "business_format",
            "description": "<p>(可选)    经营业态</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "administrative",
            "description": "<p>(可选)    行政区划分</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "market_type",
            "description": "<p>(可选)    市场类型</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>(可选)    主呼电话</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "settlement_account",
            "description": "<p>(可选)    电子结算账号</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "circle",
            "description": "<p>(可选)   是否敏感商圈</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_downgrade",
            "description": "<p>(可选)    是否有降级降档情况</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_1",
            "description": "<p>(可选)    车辆牌照1</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_2",
            "description": "<p>(可选)    车辆牌照2</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_3",
            "description": "<p>(可选)    车辆牌照3</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_photo1",
            "description": "<p>(可选)    车辆牌照图1</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_photo2",
            "description": "<p>(可选)    车辆牌照图2</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "car_photo3",
            "description": "<p>(可选)    车辆牌照图3</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "operators1",
            "description": "<p>(可选)    日常经营人1</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "license_ship1",
            "description": "<p>(可选)    与持证人关系1</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "operators2",
            "description": "<p>(可选)    日常经营人2</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "license_ship2",
            "description": "<p>(可选)    与持证人关系2</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "operators3",
            "description": "<p>(可选)    日常经营人3</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "license_ship3",
            "description": "<p>(可选)    与持证人关系3</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "special_category",
            "description": "<p>(可选)    特殊群体类别</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"longitude\":\"129.4587412\",\n    \"store_id\":1533\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"零售户信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/store.py",
    "groupTitle": "store",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/store/modifyStoreInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/task/addAudit",
    "title": "添加稽查记录",
    "version": "0.0.1",
    "name": "addAudit",
    "group": "task",
    "description": "<p>添加稽查记录</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须，零售商户必须先有数据)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector_id",
            "description": "<p>(必须，用户表中必须先有数据)    稽查人员id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "task_id",
            "description": "<p>(必须，用户表中必须先有数据)    任务分配表id</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "audit_date",
            "description": "<p>(必须)    稽查时间</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic1",
            "description": "<p>(可选)    稽查情况照片1</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic2",
            "description": "<p>(可选)    稽查情况照片2</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic3",
            "description": "<p>(可选)    稽查情况照片3</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "audit_pic4",
            "description": "<p>(可选)    稽查情况照片4</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "audit_pic5",
            "description": "<p>(可选)    稽查情况照片5</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic6",
            "description": "<p>(可选)    稽查情况照片6</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "audit_result",
            "description": "<p>(可选)   稽查结果反馈</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_note",
            "description": "<p>(可选)    稽查情况备注</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_opensale",
            "description": "<p>(可选)   是否公开摆卖</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "measures",
            "description": "<p>(可选)   采取措施</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_holdcertificate",
            "description": "<p>(可选)   是否持证经营</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_opencertificate",
            "description": "<p>(可选)   是否亮证经营</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_saleticket",
            "description": "<p>(可选)   是否销售烟票</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_saleskyprice",
            "description": "<p>(可选)   是否存在天价烟销售</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_potentially_illegal",
            "description": "<p>(可选)   是否有潜在违法行为</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "score",
            "description": "<p>(可选)    评分</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"inspector_id\":2,\n    \"task_id\":2,\n    \"audit_date\":\"2020-04-01\",\n    \"audit_pic1\":\"2451245\",\n    \"audit_pic2\":\"14586\",\n    \"audit_pic3\":\"akdkjg\",\n    \"audit_pic4\":\"sdgjg\",\n    \"audit_pic5\":\"dasgsegj\",\n    \"audit_pic6\":\"dsgkj\",\n    \"audit_result\":\"True\",\n    \"audit_note\":\"稽查good\",\n    \"is_opensale\":\"True\",\n    \"measures\":\"ORDER\",\n    \"is_holdcertificate\":\"True\",\n    \"is_opencertificate\":\"True\",\n    \"is_saleticket\":\"True\",\n    \"is_saleskyprice\":\"True\",\n    \"is_potentially_illegal\":\"True\",\n    \"score\":\"85\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"稽查记录添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n     \"sys_status\": \"FAIL\",\n     \"data\": 1,\n     \"message\": \"该任务已经完成，稽查记录已被添加\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/addAudit"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/task/addPoint",
    "title": "添加藏匿图点",
    "version": "0.0.1",
    "name": "addPoint",
    "group": "task",
    "description": "<p>添加藏匿图点</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "audit_id",
            "description": "<p>(必须)    稽查记录id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "point_x",
            "description": "<p>(可选)    标记点X坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "point_y",
            "description": "<p>(可选)    标记点X坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "note",
            "description": "<p>(可选)    标记点文字备注</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"audit_id\":1,\n    \"point_x\":\"12.452\",\n    \"point_y\":\"14.541\",\n    \"note\":\"藏钱地方在......\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"藏匿图点添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/addPoint"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/delAudit",
    "title": "删除稽查信息",
    "version": "0.0.1",
    "name": "delAudit",
    "group": "task",
    "description": "<p>删除稽查信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "audit_id",
            "description": "<p>(必须)    稽查记录id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"audit_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"稽查信息删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/delAudit"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/delPoint",
    "title": "删除藏匿图信息",
    "version": "0.0.1",
    "name": "delPoint",
    "group": "task",
    "description": "<p>删除藏匿图信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "point_id",
            "description": "<p>(必须)    藏匿图点id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"point_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": true,\n    \"message\": \"藏匿图信息删除成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/delPoint"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/getAuditInfoByStoreid",
    "title": "根据店铺id获取稽查记录信息",
    "version": "0.0.1",
    "name": "getAuditInfoByStoreid",
    "group": "task",
    "description": "<p>根据店铺id获取稽查记录信息，此接口使用了分页功能，因为是post方法，page参数通过表单形式提交</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n      \"sys_status\": \"SUCCESS\",\n      \"data\": {\n          \"data\": [\n              {\n                  \"id\": 1,\n                  \"store_id\": 5,\n                  \"inspector_id\": 2,\n                  \"task_id\": 2,\n                  \"audit_date\": \"2020-04-01\",\n                  \"audit_pic1\": \"2451245\",\n                  \"audit_pic2\": \"14586\",\n                  \"audit_pic3\": \"akdkjg\",\n                  \"audit_pic4\": \"sdgjg\",\n                  \"audit_pic5\": \"dasgsegj\",\n                  \"audit_pic6\": \"dsgkj\",\n                  \"audit_result\": true,\n                  \"audit_note\": \"稽查good\",\n                  \"is_opensale\": true,\n                  \"measures\": {\n                      \"ORDER\": \"责令整改\"\n                  },\n                  \"is_holdcertificate\": true,\n                  \"is_opencertificate\": true,\n                  \"is_saleticket\": true,\n                  \"is_saleskyprice\": true,\n                  \"is_potentially_illegal\": true,\n                  \"score\": \"85.00\"\n              }\n          ],\n          \"count\": 1\n      },\n      \"message\": \" \"\n  }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getAuditInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/getPointInfoByStoreid",
    "title": "通过零售商户id获取藏匿图信息",
    "version": "0.0.1",
    "name": "getPointInfoByStoreid",
    "group": "task",
    "description": "<p>通过零售商户id获取藏匿图信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>(必须)    页数</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "per_page",
            "description": "<p>(必须)    每页的页数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"store_id\":5,\n    \"page\":1,\n    \"per_page\":8\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"store_id\": 5,\n            \"audit_id\": 1,\n            \"point_x\": \"12.45\",\n            \"point_y\": \"14.54\",\n            \"note\": \"藏钱地方在......\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getPointInfoByStoreid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/getPointInfoByauditid",
    "title": "通过稽查记录id获取藏匿图信息",
    "version": "0.0.1",
    "name": "getPointInfoByauditid",
    "group": "task",
    "description": "<p>通过稽查记录id获取藏匿图信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "audit_id",
            "description": "<p>(必须)    稽查记录id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"audit_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"store_id\": 5,\n            \"audit_id\": 1,\n            \"point_x\": \"12.45\",\n            \"point_y\": \"14.54\",\n            \"note\": \"藏钱地方在......\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getPointInfoByauditid"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/getauditInfoByid",
    "title": "通过稽查记录id获取详细信息",
    "version": "0.0.1",
    "name": "getauditInfoByid",
    "group": "task",
    "description": "<p>通过稽查记录id获取详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "audit_id",
            "description": "<p>(必须)    稽查记录id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"audit_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 1,\n            \"store_id\": 5,\n            \"inspector_id\": 2,\n            \"task_id\": 2,\n            \"audit_date\": \"2020-04-01\",\n            \"audit_pic1\": \"2451245\",\n            \"audit_pic2\": \"14586\",\n            \"audit_pic3\": \"akdkjg\",\n            \"audit_pic4\": \"sdgjg\",\n            \"audit_pic5\": \"dasgsegj\",\n            \"audit_pic6\": \"dsgkj\",\n            \"audit_result\": true,\n            \"audit_note\": \"稽查good\",\n            \"is_opensale\": true,\n            \"measures\": {\n                \"ORDER\": \"责令整改\"\n            },\n            \"is_holdcertificate\": true,\n            \"is_opencertificate\": true,\n            \"is_saleticket\": true,\n            \"is_saleskyprice\": true,\n            \"is_potentially_illegal\": true,\n            \"score\": \"85.00\"\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getauditInfoByid"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/task/modifyAuditInfo",
    "title": "修改稽查信息",
    "version": "0.0.1",
    "name": "modifyAuditInfo",
    "group": "task",
    "description": "<p>修改稽查信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "audit_id",
            "description": "<p>(必须)    稽查记录id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(可选)    零售商户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector_id",
            "description": "<p>(可选)    稽查人员id</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "audit_date",
            "description": "<p>(可选)    稽查时间</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic1",
            "description": "<p>(可选)    稽查情况照片1</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic2",
            "description": "<p>(可选)    稽查情况照片2</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic3",
            "description": "<p>(可选)    稽查情况照片3</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "audit_pic4",
            "description": "<p>(可选)    稽查情况照片4</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "audit_pic5",
            "description": "<p>(可选)    稽查情况照片5</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_pic6",
            "description": "<p>(可选)    稽查情况照片6</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "result",
            "description": "<p>(可选)   稽查结果反馈</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "audit_note",
            "description": "<p>(可选)    稽查情况备注</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_opensale",
            "description": "<p>(可选)   是否公开摆卖</p>"
          },
          {
            "group": "Parameter",
            "type": "Enum",
            "optional": false,
            "field": "measures",
            "description": "<p>(可选)   采取措施</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_holdcertificate",
            "description": "<p>(可选)   是否持证经营</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_opencertificate",
            "description": "<p>(可选)   是否亮证经营</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_saleticket",
            "description": "<p>(可选)   是否销售烟票</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_saleskyprice",
            "description": "<p>(可选)   是否存在天价烟销售</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_potentially_illegal",
            "description": "<p>(可选)   是否有潜在违法行为</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "score",
            "description": "<p>(可选)    评分</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"audit_id\":1,\n    \"inspector_id\":4,\n    \"audit_date\":\"2020-04-01\",\n    \"audit_pic1\":\"2451245\",\n    \"audit_pic2\":\"14586\",\n    \"audit_pic3\":\"akdkjgdksgk\",\n    \"audit_pic4\":\"sdgjg\",\n    \"audit_pic5\":\"dasgsegj\",\n    \"audit_pic6\":\"dsgkj\",\n    \"audit_result\":\"False\",\n    \"audit_note\":\"哈哈，颤抖吧，违法户们\",\n    \"is_opensale\":\"True\",\n    \"measures\":\"ORDER\",\n    \"is_holdcertificate\":\"True\",\n    \"is_opencertificate\":\"True\",\n    \"is_saleticket\":\"True\",\n    \"is_saleskyprice\":\"True\",\n    \"is_potentially_illegal\":\"True\",\n    \"score\":\"85\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"稽查记录信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/modifyAuditInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/task/modifyPointInfo",
    "title": "修改藏匿图信息",
    "version": "0.0.1",
    "name": "modifyPointInfo",
    "group": "task",
    "description": "<p>修改藏匿图信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "point_id",
            "description": "<p>(必须)    藏匿图点id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(可选)    零售户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "audit_id",
            "description": "<p>(可选)    稽查记录id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "point_x",
            "description": "<p>(可选)    标记点X坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "point_y",
            "description": "<p>(可选)    标记点X坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "note",
            "description": "<p>(可选)    标记点文字备注</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"point_id\":1,\n    \"store_id\":5,\n    \"audit_id\":1,\n    \"point_x\":\"17.145\",\n    \"point_y\":\"18.541\",\n    \"note\":\"藏烟的地方在床下\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"藏匿图信息修改成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "task",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/modifyPointInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "api/uploadfile/uploadfilecaseinfo",
    "title": "案件违法信息excel上传",
    "version": "0.0.1",
    "name": "uploadfilecaseinfo",
    "group": "uploadfile",
    "description": "<p>案件违法信息excel上传</p>",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    注意 本接口将上传和解析到数据库两个接口写在一起，必须遵从以下规则\n    1.文件名必须是全英文或者全数字，不得混用，混用虽然会导入成功，但是系统会改变文件名\n    2.必须保证excel导入时sheet表名是 Sheet0\n    3.数据必须按照群里发的卷烟案件数据导入模板的样式，数据列不得调整，否则会导致导入失败\n    4.本接口只支持导入xls、 xlsx格式导入\n}\n,encoding_override=\"utf-8\"",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/uploadfile.py",
    "groupTitle": "uploadfile",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/uploadfile/uploadfilecaseinfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/addTaskInfo",
    "title": "添加任务",
    "version": "0.0.1",
    "name": "addTaskInfo",
    "group": "任务分配",
    "description": "<p>添加任务</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "role_id",
            "description": "<p>(必须)    角色id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    用户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "store_id",
            "description": "<p>(必须)    零售户id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector1_id",
            "description": "<p>(必须)    稽查人员1id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector2_id",
            "description": "<p>(可选)    稽查人员2id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector3_id",
            "description": "<p>(可选)    稽查人员3id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector4_id",
            "description": "<p>(可选)    稽查人员4id</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "inspector5_id",
            "description": "<p>(可选)    稽查人员5id</p>"
          },
          {
            "group": "Parameter",
            "type": "data",
            "optional": false,
            "field": "end_date",
            "description": "<p>(必须)    截止时间</p>"
          },
          {
            "group": "Parameter",
            "type": "bool",
            "optional": false,
            "field": "status",
            "description": "<p>(可选)    任务状态</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"role_id\":3,\n    \"user_id\":2,\n    \"store_id\":6,\n    \"inspector1_id\":1,\n    \"inspector2_id\":3,\n    \"inspector3_id\":4,\n    \"inspector4_id\":5,\n    \"end_date\":\"2020-04-15\",\n    \"status\":\"False\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": null,\n    \"message\": \"任务添加成功\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "任务分配",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/addTaskInfo"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/task/getAlltaskInfo",
    "title": "获取总任务列表",
    "version": "0.0.1",
    "name": "getAlltaskInfo",
    "group": "任务分配",
    "description": "<p>获取总任务列表,使用分页,page指定页数，per_page指定每页多少条</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    示例:http://39.96.52.170:5000/api/case/getAlltaskInfo?page=2&per_page=8  可以获取第二页的8条内容\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "任务分配",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getAlltaskInfo"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/task/getComplishtaskInfo",
    "title": "获取已完成任务列表",
    "version": "0.0.1",
    "name": "getComplishtaskInfo",
    "group": "任务分配",
    "description": "<p>获取已完成任务列表,使用分页,page指定页数，per_page指定每页多少条</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    示例:http://39.96.52.170:5000/api/case/getComplishtaskInfo?page=2&per_page=8  可以获取第二页的8条内容\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "任务分配",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getComplishtaskInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/getTaskInfoByid",
    "title": "通过任务id获取任务详细信息",
    "version": "0.0.1",
    "name": "getTaskInfoByid",
    "group": "任务分配",
    "description": "<p>通过任务id获取任务详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "task_id",
            "description": "<p>(必须)    零售商户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"task_id\":2\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n     \"sys_status\": \"SUCCESS\",\n     \"data\": [\n         {\n             \"id\": 2,\n             \"user_id\": 1,\n             \"store_id\": 5,\n             \"store_name\": \"金华市婺城区沈美香副食店\",\n             \"address\": \"金华市婺城区中村社区中南巷10幢3单元102室\",\n             \"latitude\": \"29.09\",\n             \"longitude\": \"119.66\",\n             \"end_date\": \"2020-04-02\",\n             \"status\": false\n         }\n     ],\n     \"message\": \" \"\n }",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "任务分配",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getTaskInfoByid"
      }
    ]
  },
  {
    "type": "GET",
    "url": "api/task/getunComplishtaskInfo",
    "title": "获取未完成任务列表",
    "version": "0.0.1",
    "name": "getunComplishtaskInfo",
    "group": "任务分配",
    "description": "<p>获取未完成任务列表,使用分页,page指定页数，per_page指定每页多少条</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    示例:http://39.96.52.170:5000/api/case/getunComplishtaskInfo?page=2&per_page=8  可以获取第二页的8条内容\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "任务分配",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getunComplishtaskInfo"
      }
    ]
  },
  {
    "type": "POST",
    "url": "api/task/getuncomTaskInfoByuserid",
    "title": "通过用户id获取未完成任务详细信息",
    "version": "0.0.1",
    "name": "getuncomTaskInfoByuserid",
    "group": "任务分配",
    "description": "<p>通过用户id获取未完成任务详细信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>(必须)    用户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"user_id\":1\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"sys_status\": \"SUCCESS\",\n    \"data\": [\n        {\n            \"id\": 3,\n            \"user_id\": 2,\n            \"store_id\": 6,\n            \"store_name\": \"金华市婺城区徐设波副食便利店\",\n            \"address\": \"金华市婺城区亚峰路113号\",\n            \"latitude\": \"29.09\",\n            \"longitude\": \"119.66\",\n            \"end_date\": \"2020-04-15\",\n            \"status\": false\n        },\n        {\n            \"id\": 2,\n            \"user_id\": 1,\n            \"store_id\": 5,\n            \"store_name\": \"金华市婺城区沈美香副食店\",\n            \"address\": \"金华市婺城区中村社区中南巷10幢3单元102室\",\n            \"latitude\": \"29.09\",\n            \"longitude\": \"119.66\",\n            \"end_date\": \"2020-04-02\",\n            \"status\": false\n        }\n    ],\n    \"message\": \" \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/task.py",
    "groupTitle": "任务分配",
    "sampleRequest": [
      {
        "url": "http://39.96.52.170:5000/api/task/getuncomTaskInfoByuserid"
      }
    ]
  }
] });
