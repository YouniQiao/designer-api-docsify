# clearUpApplicationData（系统接口）

## 导入模块

```TypeScript
```

## clearUpApplicationData

```TypeScript
function clearUpApplicationData(bundleName: string): Promise<void>
```

通过Bundle名称清除应用数据。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md)

**需要权限：** ohos.permission.CLEAN_APPLICATION_DATA

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## clearUpApplicationData

```TypeScript
function clearUpApplicationData(bundleName: string, callback: AsyncCallback<void>)
```

通过Bundle名称清除应用数据。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md)

**需要权限：** ohos.permission.CLEAN_APPLICATION_DATA

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
