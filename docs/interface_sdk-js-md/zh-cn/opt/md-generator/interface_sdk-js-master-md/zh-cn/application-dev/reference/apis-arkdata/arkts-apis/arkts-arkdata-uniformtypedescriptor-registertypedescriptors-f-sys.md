# registerTypeDescriptors（系统接口）

## registerTypeDescriptors

```TypeScript
function registerTypeDescriptors(typeDescriptors: Array<TypeDescriptor>): Promise<void>
```

注册一组标准化数据类型到系统中。使用Promise异步回调。注册成功后，标准化数据类型将被系统管理，可通过UDMF框架在其他应用或设备间共享和识别。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_DYNAMIC_UTD_TYPE

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-uniformTypeDescriptor-function registerTypeDescriptors(typeDescriptors: Array<TypeDescriptor>): Promise<void>--><!--Device-uniformTypeDescriptor-function registerTypeDescriptors(typeDescriptors: Array<TypeDescriptor>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typeDescriptors | Array&lt;[TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [20400003](../errorcode-udmf.md#20400003-标准化数据类型描述符内容错误) |
| [20400002](../errorcode-udmf.md#20400002-标准化数据类型描述符格式错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
