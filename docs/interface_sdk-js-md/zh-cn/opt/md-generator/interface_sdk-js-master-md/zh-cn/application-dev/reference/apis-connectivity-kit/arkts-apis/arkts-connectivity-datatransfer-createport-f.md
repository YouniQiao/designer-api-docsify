# createPort

## createPort

```TypeScript
function createPort(uuid: string): void
```

通过UUID创建可以接收数据的星闪端口。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataTransfer-function createPort(uuid: string): void--><!--Device-dataTransfer-function createPort(uuid: string): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [36100020](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100020-端口重复注册) |
| [36100021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100021-端口注册数量超出上限) |
| [36100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [36100044](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100044-禁止使用星闪标准服务uuid) |
| [36100043](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100043-无效uuid) |
