# createServer

## createServer

```TypeScript
function createServer(): Server
```

创建SSAP服务端实例。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ssap-function createServer(): Server--><!--Device-ssap-function createServer(): Server-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| [Server](arkts-connectivity-ssap-server-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
