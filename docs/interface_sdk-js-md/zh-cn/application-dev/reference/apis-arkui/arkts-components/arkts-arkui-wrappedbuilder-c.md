# WrappedBuilder

`WrappedBuilder`是`@Builder`函数的包装类，用于封装全局`@Builder`函数及其参数，实现按引用传递和动态调用。

**起始版本：** 11

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## builder

```TypeScript
builder: (...args: Args) => void
```

`@Builder`装饰的全局函数，用于生成对应的自定义构建内容。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Args | 是 |

## constructor

```TypeScript
constructor(builder: (...args: Args) => void)
```

`WrappedBuilder`的构造函数。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [builder](#builder) | (...args: Args) = & gt; void | 是 |
