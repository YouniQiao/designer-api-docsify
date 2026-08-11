# stopAdvertising

## stopAdvertising

```TypeScript
function stopAdvertising(advertisingId: number): Promise<void>
```

停止广播ID对应的广播。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-advertising-function stopAdvertising(advertisingId: int): Promise<void>--><!--Device-advertising-function stopAdvertising(advertisingId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| advertisingId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [36100040](../errorcode-nearlink-service.md#36100040-整数超出范围) |
