# unregisterThermalLevelCallback

## unregisterThermalLevelCallback

```TypeScript
function unregisterThermalLevelCallback(callback?: Callback<void>): void
```

取消订阅热档位变化时的回调提醒。使用callback异步回调。

**起始版本：** 9

<!--Device-thermal-function unregisterThermalLevelCallback(callback?: Callback<void>): void--><!--Device-thermal-function unregisterThermalLevelCallback(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
try {
    thermal.unregisterThermalLevelCallback(() => {
        console.info('unsubscribe thermal level success.');
    });
    console.info('unregister thermal level callback success.');
} catch (err) {
    console.error(`Failed to unregister thermal level callback. Code: ${err.code}, message: ${err.message}`);
}
```
