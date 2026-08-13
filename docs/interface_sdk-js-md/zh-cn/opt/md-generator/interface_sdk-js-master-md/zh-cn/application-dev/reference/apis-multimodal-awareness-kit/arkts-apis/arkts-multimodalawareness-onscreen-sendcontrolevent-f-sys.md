# sendControlEvent（系统接口）

## sendControlEvent

```TypeScript
function sendControlEvent(event: ControlEvent): Promise<void>
```

在需要控制的窗口在桌面上时，在调用[onScreen.getPageContent](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md#getPageContent（系统接口）)后，根据其返回的段落信息，调用该接口发送屏上控制事件。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SIMULATE_USER_INPUT

<!--Device-onScreen-function sendControlEvent(event: ControlEvent): Promise<void>--><!--Device-onScreen-function sendControlEvent(event: ControlEvent): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [ControlEvent](arkts-multimodalawareness-onscreen-controlevent-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000005](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000005-目标未找到) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
