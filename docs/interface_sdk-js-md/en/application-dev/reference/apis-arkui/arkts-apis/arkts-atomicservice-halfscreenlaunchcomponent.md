# @ohos.atomicservice.HalfScreenLaunchComponent(Defines the halfScreen launch component)

###### Child Components
 Not supported
 ###### Attributes
 The universal attributes are not supported.


## Modules to Import

```TypeScript
import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [HalfScreenLaunchComponent](arkts-arkui-atomicservice-halfscreenlaunchcomponent-halfscreenlaunchcomponent-s.md) | **HalfScreenLaunchComponent** is a component designed for launching atomic services in half screen. If the invoked application (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in half-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner. |

## Examples

In the process list on the right, select the process of the launched atomic service. The package name has embeddable within its suffix segment.

```TypeScript
import { HalfScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  appId: string = "576****************"; // Application ID for the atomic service.

  build() {
    Column() {
      HalfScreenLaunchComponent({
        appId: this.appId,
        options: {},
        onTerminated:  (info:TerminationInfo)=> {
          console.info('onTerminated info = '+ info.want);
        },
        onError: (err) => {
          console.error(" onError code: " + err.code + ", message: ", err.message);
        },
        onReceive: (data) => {
          console.info("onReceive, data: " + data['ohos.atomicService.window']);
        }
      }) {
        Column() {
          Image($r('app.media.app_icon'))
          Text('Start top-up')
        }.width("80vp").height("80vp").margin({bottom:30})
      } // Pass content through the trailing closure.
    }
  }

}
```
