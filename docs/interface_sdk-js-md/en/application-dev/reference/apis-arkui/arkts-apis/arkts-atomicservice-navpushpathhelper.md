# @ohos.atomicservice.NavPushPathHelper(Defines provides a push method for the target page in the routing table.)

###### Child Components
 Not supported
 ###### Attributes
 The universal attributes are not supported.
 ###### Events
 The universal events are not supported.


## Modules to Import

```TypeScript
import { NavPushPathHelper } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [NavPushPathHelper](arkts-arkui-atomicservice-navpushpathhelper-navpushpathhelper-c.md) | On the initial launch, the atomic service only downloads and installs the main package and its dependencies. Therefore, if the NavDestination resides in a different HSP subpackage that is not a dependency of the main package, you'll need to use **NavPushPathHelper** to download and install the corresponding HSP subpackage first. After that, push the specified **NavDestination** page information onto the stack. This way, you enable Navigation to support dynamic loading of the HSP subpackage before the navigation occurs. |

## Examples

Main package:

```TypeScript
// Index.ets
import { NavPushPathHelper } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct NavigationExample {
  pageInfo: NavPathStack = new NavPathStack();
  helper: NavPushPathHelper = new NavPushPathHelper(this.pageInfo);

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.helper.pushPath('hsptest1', { name: 'pageOne' }, false)
              .catch((error: BusinessError) => {
              console.error(`[pushPath]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.error(`[pushPath]success.`);
            }); // Push the NavDestination page specified by name to the navigation stack.
          })
      }
    }.title('NavIndex')
  }
}
```

Subpackage hsptest1:

```TypeScript
// PageOne.ets
import { NavPushPathHelper } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class TmpClass {
  count: number = 10;
}

class ParamWithOp {
  operation: number = 1;
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne();
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  helper: NavPushPathHelper = new NavPushPathHelper(this.pageInfo);
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10)

        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.pushPath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '[pushPath]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}).catch((error: BusinessError) => {
              console.error(`[pushPath]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[pushPath]success.`);
            });
          })

        Button('pushPath with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.pushPath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '[pushPath with NavigationOptions]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
              console.error(`[pushPath with NavigationOptions]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[pushPath with NavigationOptions]success.`);
            });
          })

        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.pushPathByName('hsptest2', 'pageTwo', tmp, (popInfo) => {
              this.message = '[pushPathByName]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }).catch((error: BusinessError) => {
              console.error(`[pushPathByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[pushPathByName]success.`);
            });
          })

        Button('pushPathByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.pushPathByName('hsptest2', 'pageTwo', tmp, true)
            .catch((error: BusinessError) => {
              console.error(`[pushPathByNameWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[pushPathByNameWithoutOnPop]success.`);
            });
          })

        Button('pushDestination', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass()
            this.helper.pushDestination('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '[pushDestination]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}).catch((error: BusinessError) => {
              console.error(`[pushDestination]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.error(`[pushDestination]success.`);
            });
          })

        Button('pushDestination with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.pushDestination('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '[pushDestination with NavigationOptions]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
              console.error(`[pushDestination with NavigationOptions]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.error(`[pushDestination with NavigationOptions]success.`);
            });
          })

        Button('pushDestinationByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass()
            this.helper.pushDestinationByName('hsptest2','pageTwo', tmp, (popInfo) => {
              this.message = '[pushDestinationByName]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }).catch((error: BusinessError) => {
              console.error(`[pushDestinationByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.error(`[pushDestinationByName]success.`);
            });
          })

        Button('pushDestinationByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass()
            this.helper.pushDestinationByName('hsptest2','pageTwo', tmp, true)
              .catch((error: BusinessError) => {
                console.error(`[pushDestinationByNameWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
              }).then(() => {
              console.error(`[pushDestinationByNameWithoutOnPop]success.`);
            });
          })

        Button('replacePath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.replacePath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '[replacePath]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}).catch((error: BusinessError) => {
              console.error(`[replacePath]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[replacePath]success.`);
            });
          })

        Button('replacePath with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.replacePath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '[replacePath with NavigationOptions]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
              console.error(`[replacePath with NavigationOptions]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[replacePath with NavigationOptions]success.`);
            });
          })

        Button('replacePathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.replacePathByName('hsptest2', 'pageTwo', tmp)
              .catch((error: BusinessError) => {
              console.error(`[replacePathByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.info(`[replacePathByName]success.`);
            });
          })

      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop({ number: 1 }) // Pop the top element out of the navigation stack.
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
      this.helper = new NavPushPathHelper(this.pageInfo);
    })
  }
}
```

Configure {"routerMap": "$profile:route_map"} in the project configuration file module.json5. The configuration in the route_map.json file is as follows:

```TypeScript
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

Subpackage hsptest2:

```TypeScript
// PageTwo.ets

class resultClass {
  constructor(count: number) {
    this.count = count;
  }
  count: number = 10
}

@Builder
export function PageTwoBuilder() {
  PageTwo()
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack()

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop(new resultClass(1)); // Return to the previous page and pass in the processing result to the onPop callback of push.
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onBackPressed(() => {
      this.pathStack.pop(new resultClass(0)); // Return to the previous page and pass in the processing result to the onPop callback of push.
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack
    })
  }
}
```

Configure {"routerMap": "$profile:route_map"} in the project configuration file module.json5. The configuration in the route_map.json file is as follows:

```TypeScript
{
  "routerMap": [
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder",
      "data": {
        "description": "this is pageTwo"
      }
    }
  ]
}
```
