# @ohos.data.cloudExtension

端云共享Extension，提供第三方厂商适配共享云服务的能力。 通过实现端云共享Extension提供的接口，将端侧的数据共享到服务端，实现端云共享的发起、取消或退出，更改共享数据的操作权限、查询共享参与者、根据共享邀请码查询共享参与者、确认或更改共享邀请，并支持返回共享云服务的相关结果。 其中，端云共享资源标识是指：对于应用发起共享的每一条数据记录，该条数据在进行端云同步时会生成唯一的共享资源标识（字符串类型的值），此标识作为该条数据记录共享时的识别标识。 端云共享参与者是指：共享发起者根据好友列表选中的参与当前数据共享的所有人员。 端云共享邀请码是指：共享发起后，在共享的服务端会生成当前共享操作的邀请码，并将该邀请码附加到当前共享邀请中，通过推送消息推送到被邀请者的设备端，被邀请者可以通过该邀请码进行邀请的确认。 同步云是指：端云同步的服务端，即同应用同账号跨设备的同步。 共享云是指：端云共享的服务端，即同应用跨账号跨设备的共享。

**起始版本：** 23

<!--Device-unnamed-declare namespace cloudExtension--><!--Device-unnamed-declare namespace cloudExtension-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

## 导入模块

```TypeScript
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createAssetLoaderStub](arkts-arkdata-cloudextension-createassetloaderstub-f-sys.md#createassetloaderstub系统接口) |
| [createCloudDBStub](arkts-arkdata-cloudextension-createclouddbstub-f-sys.md#createclouddbstub系统接口) |
| [createCloudServiceStub](arkts-arkdata-cloudextension-createcloudservicestub-f-sys.md#createcloudservicestub系统接口) |
| [createShareServiceStub](arkts-arkdata-cloudextension-createshareservicestub-f-sys.md#createshareservicestub系统接口) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AppBriefInfo](arkts-arkdata-cloudextension-appbriefinfo-i-sys.md) |
| [AppSchema](arkts-arkdata-cloudextension-appschema-i-sys.md) |
| [AssetLoader](arkts-arkdata-cloudextension-assetloader-i-sys.md) |
| [CloudAsset](arkts-arkdata-cloudextension-cloudasset-i-sys.md) |
| [CloudDB](arkts-arkdata-cloudextension-clouddb-i-sys.md) |
| [CloudData](arkts-arkdata-cloudextension-clouddata-i-sys.md) |
| [CloudInfo](arkts-arkdata-cloudextension-cloudinfo-i-sys.md) |
| [CloudService](arkts-arkdata-cloudextension-cloudservice-i-sys.md) |
| [Database](arkts-arkdata-cloudextension-database-i-sys.md) |
| [ExtensionValue](arkts-arkdata-cloudextension-extensionvalue-i-sys.md) |
| [Field](arkts-arkdata-cloudextension-field-i-sys.md) |
| [LockInfo](arkts-arkdata-cloudextension-lockinfo-i-sys.md) |
| [Result](arkts-arkdata-cloudextension-result-i-sys.md) |
| [ServiceInfo](arkts-arkdata-cloudextension-serviceinfo-i-sys.md) |
| [ShareCenter](arkts-arkdata-cloudextension-sharecenter-i-sys.md) |
| [SubscribeId](arkts-arkdata-cloudextension-subscribeid-i-sys.md) |
| [SubscribeInfo](arkts-arkdata-cloudextension-subscribeinfo-i-sys.md) |
| [Table](arkts-arkdata-cloudextension-table-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ErrorCode](arkts-arkdata-cloudextension-errorcode-e-sys.md) |
| [FieldType](arkts-arkdata-cloudextension-fieldtype-e-sys.md) |
| [Flag](arkts-arkdata-cloudextension-flag-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [CloudAssets](arkts-arkdata-cloudextension-cloudassets-t-sys.md) |
| [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md) |
<!--DelEnd-->
