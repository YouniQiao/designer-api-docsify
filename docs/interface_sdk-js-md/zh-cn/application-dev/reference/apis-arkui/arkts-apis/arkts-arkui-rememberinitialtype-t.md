# RememberInitialType

```TypeScript
type RememberInitialType<T> = (() => T) | T
```

状态变量初始值入参类型。基础类型使用类型T直接传入； 复杂类型（interface、class和包含Array、Map、Set和Date的内置类型）使用回调（() =&gt; T）初始化能避免重复创建实例，性能更高。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 |
| --- |
| () = & gt; T) |
| T |
