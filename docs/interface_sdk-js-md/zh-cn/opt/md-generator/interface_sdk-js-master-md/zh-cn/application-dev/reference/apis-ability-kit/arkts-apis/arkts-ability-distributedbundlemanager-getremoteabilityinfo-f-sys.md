# getRemoteAbilityInfo（系统接口）

## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementName: ElementName, callback: AsyncCallback<RemoteAbilityInfo>): void
```

获取由elementName指定的远程设备上的应用的AbilityInfo信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName, callback: AsyncCallback<RemoteAbilityInfo>): void--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName, callback: AsyncCallback<RemoteAbilityInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RemoteAbilityInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        {
            deviceId: '1',
            bundleName: 'com.example.application',
            abilityName: 'EntryAbility'
        }, (err: BusinessError, data: distributedBundleManager.RemoteAbilityInfo) => {
            if (err) {
                console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
            } else {
                console.info('Operation succeed:' + JSON.stringify(data));
            }
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementName: ElementName): Promise<RemoteAbilityInfo>
```

获取由elementName指定的远程设备上的应用的AbilityInfo信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName): Promise<RemoteAbilityInfo>--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName): Promise<RemoteAbilityInfo>-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RemoteAbilityInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        {
            deviceId: '1',
            bundleName: 'com.example.application',
            abilityName: 'EntryAbility'
        }).then((data: distributedBundleManager.RemoteAbilityInfo) => {
            console.info('Operation succeed:' + JSON.stringify(data));
        }).catch((err: BusinessError) => {
            console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementNames: Array<ElementName>, callback: AsyncCallback<Array<RemoteAbilityInfo>>): void
```

获取由elementName指定的远程设备上的应用的AbilityInfo数组信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>, callback: AsyncCallback<Array<RemoteAbilityInfo>>): void--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>, callback: AsyncCallback<Array<RemoteAbilityInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-i.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;RemoteAbilityInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        [
            {
                deviceId: '1',
                bundleName: 'com.example.application1',
                abilityName: 'EntryAbility1'
            },
            {
                deviceId: '1',
                bundleName: 'com.example.application2',
                abilityName: 'EntryAbility'
            }
        ], (err: BusinessError, data: distributedBundleManager.RemoteAbilityInfo[]) => {
          if (err) {
            console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
          } else {
            console.info('Operation succeed:' + JSON.stringify(data));
          }
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>
```

获取由elementName指定的远程设备上的应用的AbilityInfo数组信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;RemoteAbilityInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        [
            {
                deviceId: '1',
                bundleName: 'com.example.application',
                abilityName: 'EntryAbility'
            },
            {
                deviceId: '1',
                bundleName: 'com.example.application2',
                abilityName: 'EntryAbility'
            }
        ]).then((data: distributedBundleManager.RemoteAbilityInfo[]) => {
            console.info('Operation succeed:' + JSON.stringify(data));
        }).catch((err: BusinessError) => {
            console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementName: ElementName, locale: string, callback: AsyncCallback<RemoteAbilityInfo>): void
```

获取由elementName和locale指定的远程设备上的应用的AbilityInfo信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName, locale: string, callback: AsyncCallback<RemoteAbilityInfo>): void--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName, locale: string, callback: AsyncCallback<RemoteAbilityInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| locale | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RemoteAbilityInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        {
            deviceId: '1',
            bundleName: 'com.example.application',
            abilityName: 'EntryAbility'
        }, 'zh-Hans-CN', (err: BusinessError, data: distributedBundleManager.RemoteAbilityInfo) => {
          if (err) {
            console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
          } else {
            console.info('Operation succeed:' + JSON.stringify(data));
          }
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementName: ElementName, locale: string): Promise<RemoteAbilityInfo>
```

获取由elementName和locale指定的远程设备上的应用的AbilityInfo信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName, locale: string): Promise<RemoteAbilityInfo>--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementName: ElementName, locale: string): Promise<RemoteAbilityInfo>-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| locale | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RemoteAbilityInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        {
            deviceId: '1',
            bundleName: 'com.example.application',
            abilityName: 'EntryAbility'
        }, 'zh-Hans-CN').then((data: distributedBundleManager.RemoteAbilityInfo) => {
            console.info('Operation succeed:' + JSON.stringify(data));
        }).catch((err: BusinessError) => {
            console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementNames: Array<ElementName>, locale: string, callback: AsyncCallback<Array<RemoteAbilityInfo>>): void
```

获取由elementName和locale指定的远程设备上的应用的AbilityInfo数组信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>, locale: string, callback: AsyncCallback<Array<RemoteAbilityInfo>>): void--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>, locale: string, callback: AsyncCallback<Array<RemoteAbilityInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-i.md)&gt; | 是 |
| locale | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;RemoteAbilityInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        [
            {
                deviceId: '1',
                bundleName: 'com.example.application1',
                abilityName: 'EntryAbility1'
            },
            {
                deviceId: '1',
                bundleName: 'com.example.application2',
                abilityName: 'EntryAbility'
            }
        ], 'zh-Hans-CN', (err: BusinessError, data: distributedBundleManager.RemoteAbilityInfo[]) => {
          if (err) {
           console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
          } else {
            console.info('Operation succeed:' + JSON.stringify(data));
          }
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```


## getRemoteAbilityInfo

```TypeScript
function getRemoteAbilityInfo(elementNames: Array<ElementName>, locale: string): Promise<Array<RemoteAbilityInfo>>
```

获取由elementName和locale指定的远程设备上的应用的AbilityInfo数组信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>, locale: string): Promise<Array<RemoteAbilityInfo>>--><!--Device-distributedBundleManager-function getRemoteAbilityInfo(elementNames: Array<ElementName>, locale: string): Promise<Array<RemoteAbilityInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.DistributedBundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-i.md)&gt; | 是 |
| locale | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;RemoteAbilityInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700027](../errorcode-bundle.md#17700027-分布式服务未启动) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700007](../errorcode-bundle.md#17700007-输入的设备id有误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedBundleManager.getRemoteAbilityInfo(
        [
            {
                deviceId: '1',
                bundleName: 'com.example.application',
                abilityName: 'EntryAbility'
            },
            {
                deviceId: '1',
                bundleName: 'com.example.application2',
                abilityName: 'EntryAbility'
            }
        ], 'zh-Hans-CN').then((data: distributedBundleManager.RemoteAbilityInfo[]) => {
            console.info('Operation succeed:' + JSON.stringify(data));
        }).catch((err: BusinessError) => {
            console.error(`Operation failed: error code is ${err.code}  and error message is ${err.message}`);
        });
} catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Operation failed: error code is ${code}  and error message is ${message}`);
}
```
