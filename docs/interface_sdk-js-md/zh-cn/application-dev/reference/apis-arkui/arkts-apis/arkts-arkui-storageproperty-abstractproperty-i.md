# AbstractProperty

Define AbstractProperty&lt;T&gt; interface.AbstractProperty can be understood as a handler or an alias to a property inside LocalStorage / AppStorage singleton allows to read the value with

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## get

```TypeScript
get(): T
```

读取AppStorage/ LocalStorage中所引用属性的数据。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| T |

## info

```TypeScript
default info(): string
```

读取AppStorage/ LocalStorage中所引用属性的属性名。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## onChange

```TypeScript
default onChange(onChangeFunc: OnChangeType<T> | undefined): void
```

注册AppStorage/ LocalStorage中所引用属性变化的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onChangeFunc | [OnChangeType](arkts-arkui-onchangetype-t.md)&lt;T&gt; \| undefined | 是 |

## set

```TypeScript
default set(newValue: T): void
```

更新AppStorage/ LocalStorage中所引用属性的数据，newValue必须是T类型，可以为null或 undefined。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |
