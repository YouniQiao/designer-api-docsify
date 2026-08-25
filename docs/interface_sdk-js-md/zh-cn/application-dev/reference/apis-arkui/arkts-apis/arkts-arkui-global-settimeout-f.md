# setTimeout

## 导入模块

```TypeScript
```

## setTimeout

```TypeScript
export declare function setTimeout(handler: Function | string, delay?: number, ...arguments: any[]): number
```

设置一个定时器，该定时器在定时器到期后执行一个函数。 该定时器在回调被执行后自动删除，或使用clearTimeout()接口手动删除。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | Function \| string | 是 |
| delay | number | 否 |
| [arguments](../../apis-arkts/arkts-apis/arkts-arkts-taskpool-task-c.md) | any[] | 是 |

**返回值：**

| 类型 |
| --- |
| number |
