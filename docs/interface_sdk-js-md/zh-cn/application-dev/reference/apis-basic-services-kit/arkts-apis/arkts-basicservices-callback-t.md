# Callback

```TypeScript
export type Callback<T> = (data: T) => void
```

通用回调函数。开发者在使用时，可自定义data的类型，回调将返回对应类型的信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | T | 是 |
