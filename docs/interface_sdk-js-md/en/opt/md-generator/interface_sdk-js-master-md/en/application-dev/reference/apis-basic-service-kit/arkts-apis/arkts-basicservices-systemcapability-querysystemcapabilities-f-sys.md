# querySystemCapabilities (System API)

## Modules to Import

```TypeScript
import { systemCapability } from '@kit.BasicServicesKit';
```

## querySystemCapabilities

```TypeScript
function querySystemCapabilities(callback: AsyncCallback<string>): void
```

Get System Capability.

**Since:** 9

<!--Device-systemCapability-function querySystemCapabilities(callback: AsyncCallback<string>): void--><!--Device-systemCapability-function querySystemCapabilities(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Developtools.Syscap

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
try {
    systemCapability.querySystemCapabilities((err:Error, data:string) => {
    if (err == undefined) {
        console.info("get system capabilities:" + data);
    } else {
        console.error(" get system capabilities err:" + err);
    }});
}catch(e){
    console.error("get unexpected error: " + e);
}
```


## querySystemCapabilities

```TypeScript
function querySystemCapabilities(): Promise<string>
```

Get System Capability.

**Since:** 9

<!--Device-systemCapability-function querySystemCapabilities(): Promise<string>--><!--Device-systemCapability-function querySystemCapabilities(): Promise<string>-End-->

**System capability:** SystemCapability.Developtools.Syscap

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## Examples

```TypeScript
try {
    systemCapability.querySystemCapabilities().then((value:string) => {
        console.info("get system capabilities: " + value);
    }).catch((err:Error) => {
        console.error("get system capabilities error: " + err);
    });
}catch(e){
    console.error("get unexpected error: " + e);
}
```
