# getNameForUid

## 导入模块

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getNameForUid

```TypeScript
function getNameForUid(uid: number, callback: AsyncCallback<string>): void
```

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md)

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |


## getNameForUid

```TypeScript
function getNameForUid(uid: number): Promise<string>
```

通过uid获取对应的Bundle名称，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |
