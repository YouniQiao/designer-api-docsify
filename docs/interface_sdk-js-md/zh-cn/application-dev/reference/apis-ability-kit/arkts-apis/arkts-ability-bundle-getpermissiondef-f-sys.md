# getPermissionDef（系统接口）

## 导入模块

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getPermissionDef

```TypeScript
function getPermissionDef(permissionName: string, callback: AsyncCallback<PermissionDef>): void
```

按权限名称获取权限的详细信息，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissionName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionDef](arkts-ability-permissiondef-depr-i-sys.md)&gt; | 是 |


## getPermissionDef

```TypeScript
function getPermissionDef(permissionName: string): Promise<PermissionDef>
```

按权限名称获取权限的详细信息，使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissionName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PermissionDef](arkts-ability-permissiondef-depr-i-sys.md)&gt; |
