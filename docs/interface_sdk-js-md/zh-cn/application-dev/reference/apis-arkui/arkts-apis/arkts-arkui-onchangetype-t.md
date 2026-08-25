# OnChangeType

```TypeScript
export type OnChangeType<T> = (propertyName: string, newValue: T) => void
```

注册AppStorage/ LocalStorage中所引用属性变化事件的回调函数类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propertyName | string | 是 |
| newValue | T | 是 |
