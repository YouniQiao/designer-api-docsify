# subscribeThermalLevel

## subscribeThermalLevel

```TypeScript
function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void
```

订阅热档位变化时的回调提醒。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [thermal.registerThermalLevelCallback](arkts-basicservices-thermal-registerthermallevelcallback-f.md#registerthermallevelcallback)

<!--Device-thermal-function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void--><!--Device-thermal-function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void-End-->

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;ThermalLevel&gt; | 是 |

## 示例

```TypeScript
thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    if (err) {
        console.error('subscribe thermal level failed, err: ' + err);
        return;
    }
    console.info('thermal level is: ' + level);
});
```
