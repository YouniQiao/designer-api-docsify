# stopDeviceLogging（系统接口）

## stopDeviceLogging

```TypeScript
function stopDeviceLogging(): Promise<void>
```

停止当前设备日志写入。结果通过Promise异步回调方式返回。

**起始版本：** 13

<!--Device-avSession-function stopDeviceLogging(): Promise<void>--><!--Device-avSession-function stopDeviceLogging(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
avSession.stopDeviceLogging().then(() => {
  console.info('Succeeded in stopping casting.');
});
```
