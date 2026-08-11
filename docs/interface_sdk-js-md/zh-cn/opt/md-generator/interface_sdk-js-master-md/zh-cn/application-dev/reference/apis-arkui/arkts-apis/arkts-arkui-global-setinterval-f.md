# setInterval

## setInterval

```TypeScript
export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number
```

重复调用一个函数，在每次调用之间具有固定的时间延迟。删除该定时器需手动调用clearInterval()接口。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number--><!--Device-unnamed-export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | Function \| string | 是 |
| delay | number | 是 |
| arguments | any[] | 是 |

**返回值：**

| 类型 |
| --- |
| number |
