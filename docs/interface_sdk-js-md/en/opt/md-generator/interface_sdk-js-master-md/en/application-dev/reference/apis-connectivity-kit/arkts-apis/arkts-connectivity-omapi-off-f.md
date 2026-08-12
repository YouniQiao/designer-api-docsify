# off

## Modules to Import

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
```

## off('stateChanged')

```TypeScript
function off(type: 'stateChanged', callback?: Callback<ServiceState>): void
```

Unsubscribe the service state changed event.

**Since:** 18

<!--Device-omapi-function off(type: 'stateChanged', callback?: Callback<ServiceState>): void--><!--Device-omapi-function off(type: 'stateChanged', callback?: Callback<ServiceState>): void-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService: omapi.SEService;
function seStateOnCb(data: omapi.ServiceState) {
    hilog.info(0x0000, 'testTag', 'omapi.on ServiceState: %{public}s', JSON.stringify(data));
}

function seStateOffCb(data: omapi.ServiceState) {
    hilog.info(0x0000, 'testTag', 'omapi.off ServiceState: %{public}s', JSON.stringify(data));

}

function secureElementDemo() {
    try{
        omapi.createService().then((data) => {
            seService = data;
            if (seService == undefined || !seService.isConnected()) {
                hilog.error(0x0000, 'testTag', 'seservice state disconnected');
                return;
            }
            hilog.info(0x0000, 'testTag', 'seservice state connected');
        }).catch((error : BusinessError)=> {
            hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
        });
        omapi.on('stateChanged', seStateOnCb);
    } catch (error) {
        if (error as BusinessError) {
            hilog.error(0x0000, 'testTag', 'omapi on error %{public}s', JSON.stringify(error));
        }
    }
    try{
        omapi.off('stateChanged', seStateOffCb);
    } catch (error) {
        if (error as BusinessError) {
            hilog.error(0x0000, 'testTag', 'omapi off error %{public}s', JSON.stringify(error));
        }
    }
}
```
