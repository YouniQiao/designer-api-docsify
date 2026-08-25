# isRamConstrainedDevice

## 导入模块

```TypeScript
```

## isRamConstrainedDevice

```TypeScript
function isRamConstrainedDevice(): Promise<boolean>
```

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md)

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |


## isRamConstrainedDevice

```TypeScript
function isRamConstrainedDevice(callback: AsyncCallback<boolean>): void
```

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md)

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |
