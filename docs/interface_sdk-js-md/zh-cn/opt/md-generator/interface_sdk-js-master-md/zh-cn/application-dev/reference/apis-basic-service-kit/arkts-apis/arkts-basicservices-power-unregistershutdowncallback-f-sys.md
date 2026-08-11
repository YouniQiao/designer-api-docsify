# unregisterShutdownCallback（系统接口）

## unregisterShutdownCallback

```TypeScript
function unregisterShutdownCallback(callback?: Callback<void>): void
```

取消订阅电源关机或重启的回调提醒。使用callback同步回调。

**起始版本：** 23

**需要权限：** ohos.permission.REBOOT

<!--Device-power-function unregisterShutdownCallback(callback?: Callback<void>): void--><!--Device-power-function unregisterShutdownCallback(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    power.unregisterShutdownCallback(() => {
        console.info('unsubscribe shutdown success.');
    });
    console.info('unregister shutdown callback success.');
} catch (err) {
    console.error(`Failed to unregister shutdown callback. Code: ${err.code}, message: ${err.message}`);
}
```
