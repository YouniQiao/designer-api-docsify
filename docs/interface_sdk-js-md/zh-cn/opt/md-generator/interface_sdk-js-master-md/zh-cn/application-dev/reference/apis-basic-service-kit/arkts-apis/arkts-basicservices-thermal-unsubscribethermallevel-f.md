# unsubscribeThermalLevel

## unsubscribeThermalLevel

```TypeScript
function unsubscribeThermalLevel(callback?: AsyncCallback<void>): void
```

取消订阅热档位变化时的回调提醒。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [thermal.unregisterThermalLevelCallback](arkts-basicservices-thermal-unregisterthermallevelcallback-f.md#unregisterthermallevelcallback)

<!--Device-thermal-function unsubscribeThermalLevel(callback?: AsyncCallback<void>): void--><!--Device-thermal-function unsubscribeThermalLevel(callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## 示例

```TypeScript
thermal.unsubscribeThermalLevel(() => {
    console.info('unsubscribe thermal level success.');
});
```
