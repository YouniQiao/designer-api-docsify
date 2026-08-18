# off_formUninstall（系统接口）

## 导入模块

```TypeScript
```

## off_formUninstall

```TypeScript
function off(type: 'formUninstall', callback?: Callback<string>): void
```

取消订阅卡片卸载事件。使用callback异步回调。 > **说明：** > > 卡片卸载与卡片移除不同。当应用卸载时，对应的卡片会自动卸载。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-form-formhost-offformuninstall-f-sys.md#offformuninstall)

<!--Device-formHost-function off(type: 'formUninstall', callback?: Callback<string>): void--><!--Device-formHost-function off(type: 'formUninstall', callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'formUninstall' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |
