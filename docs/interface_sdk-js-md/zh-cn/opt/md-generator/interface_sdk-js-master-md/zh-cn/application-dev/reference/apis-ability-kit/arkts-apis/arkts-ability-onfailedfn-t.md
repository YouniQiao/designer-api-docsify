# OnFailedFn

```TypeScript
type OnFailedFn = (code: number) => void
```

与指定的后台服务建立连接失败时，会触发该回调，返回连接失败的错误码。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-type OnFailedFn = (code: int) => void--><!--Device-unnamed-type OnFailedFn = (code: int) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
