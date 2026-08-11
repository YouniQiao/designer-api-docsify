# clearTimeout

## clearTimeout

```TypeScript
export declare function clearTimeout(timeoutID?: number): void
```

取消通过调用setTimeout()建立的定时器。定时器对象保存在创建它的线程内，删除定时器时需要在该线程中进行。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export declare function clearTimeout(timeoutID?: number): void--><!--Device-unnamed-export declare function clearTimeout(timeoutID?: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeoutID | number | 否 |
