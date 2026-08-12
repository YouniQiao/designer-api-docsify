# createClient

## createClient

```TypeScript
function createClient(address: string): Client
```

创建SSAP客户端实例。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ssap-function createClient(address: string): Client--><!--Device-ssap-function createClient(address: string): Client-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| address | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Client](arkts-connectivity-ssap-client-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [36100041](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100041-无效地址) |
