# setRttCapability（系统接口）

## 导入模块

```TypeScript
```

## setRttCapability

```TypeScript
function setRttCapability(accountId: number, isEnable: boolean): Promise<void>
```

设置rtt功能

**起始版本：** 23

**需要权限：** ohos.permission.PLACE_CALL

<!--Device-call-function setRttCapability(accountId: int, isEnable: boolean): Promise<void>--><!--Device-call-function setRttCapability(accountId: int, isEnable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | number | 是 |
| isEnable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
