# clearInterval

## clearInterval

```TypeScript
export declare function clearInterval(intervalID?: number): void
```

取消通过setInterval()设置的重复定时任务。定时器对象保存在创建它的线程内，删除定时器时需要在该线程中进行。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export declare function clearInterval(intervalID?: number): void--><!--Device-unnamed-export declare function clearInterval(intervalID?: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| intervalID | number | 否 |
