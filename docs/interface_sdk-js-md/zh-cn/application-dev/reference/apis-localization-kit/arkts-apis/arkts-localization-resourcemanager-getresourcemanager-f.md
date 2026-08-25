# getResourceManager

## 导入模块

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## getResourceManager

```TypeScript
export function getResourceManager(callback: AsyncCallback<ResourceManager>): void
```

获取当前应用的资源管理对象。使用callback异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | AsyncCallback&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; | 是 |


## getResourceManager

```TypeScript
export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void
```

获取指定应用的资源管理对象。使用callback异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | AsyncCallback&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; | 是 |


## getResourceManager

```TypeScript
export function getResourceManager(): Promise<ResourceManager>
```

获取当前应用的资源管理对象。使用Promise异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; |


## getResourceManager

```TypeScript
export function getResourceManager(bundleName: string): Promise<ResourceManager>
```

获取指定应用的资源管理对象。使用Promise异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; |
