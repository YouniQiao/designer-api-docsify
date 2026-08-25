# setInterval

## 导入模块

```TypeScript
```

## setInterval

```TypeScript
function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int
```

按照delayMs间隔重复调用回调函数。首次调用将在delayMs之后执行。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | Function | 是 |
| delayMs | int \| null \| undefined | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| int |
