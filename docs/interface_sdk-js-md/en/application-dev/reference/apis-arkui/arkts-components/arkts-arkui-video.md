# Video

The **Video** component is used to play a video and control its playback. > **NOTE** > > The **Video** component provides only simple video playback features. For complex video playback control > scenarios, consider using the [AVPlayer](../../apis-media-kit/arkts-apis/arkts-media-media-avplayer-i.md) APIs in conjunction with the > XComponent component. > When using **expandSafeArea** to extend into safe areas, the **Video** component's content display area does not > support expansion. > > **Required Permissions** > > To use online videos, you must apply for the ohos.permission.INTERNET permission. For details about how to apply > for a permission, see [Declaring Permissions](../../../security/AccessToken/declare-permissions.md). > > **Child Components** > > Not supported.

## Video

```TypeScript
Video(value: VideoOptions)
```

Defines the constructor of video component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VideoOptions](arkts-arkui-videooptions-i.md) | Yes | Video information. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |

### Enums

| Name | Description |
| --- | --- |

## Examples

This example covers the basic features of video playback, including how to manage the control bar, use preview images, handle autoplay, adjust the playback speed, respond to keyboard shortcuts (since API version 15, [enableShortcutKey](arkts-arkui-video-attribute.md#enableshortcutkey) can be used for enabling keyboard shortcut response), and operate the controller for playback control. Additionally, it demonstrates how to implement first frame display (since API version 18, [posterOptions](#posteroptions18) can be used for setting first frame display options). Since API version 21, posterOptions supports configuring transition animation effects for video preview image content changes through the contentTransitionEffect parameter of [PosterOptions](#posteroptions18). along with related state callbacks.

```TypeScript
// xxx.ets
@Entry
@Component
struct VideoCreateComponent {
  // Replace $rawfile('video1.mp4') and $r('app.media.poster1') with the resource files you use.
  @State videoSrc: Resource = $rawfile('video1.mp4');
  @State previewUri: Resource = $r('app.media.poster1');
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  @State isAutoPlay: boolean = false;
  @State showControls: boolean = true;
  @State isShortcutKeyEnabled: boolean = false;
  @State showFirstFrame: boolean = false;
  controller: VideoController = new VideoController();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri, // Set the preview image.
        currentProgressRate: this.curRate, // Set the playback speed.
        controller: this.controller,
        posterOptions: { showFirstFrame: this.showFirstFrame, contentTransitionEffect: ContentTransitionEffect.OPACITY } // Disable the first frame display and set the preview image fade-in and fade-out animation.
      })
        .width('100%')
        .height(600)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .enableShortcutKey(this.isShortcutKeyEnabled)
        .onStart(() => {
          console.info('onStart');
        })
        .onPause(() => {
          console.info('onPause');
        })
        .onFinish(() => {
          console.info('onFinish');
        })
        .onError(() => {
          console.info('onError');
        })
        .onStop(() => {
          console.info('onStop');
        })
        .onPrepared((e?: DurationObject) => {
          if (e != undefined) {
            console.info('onPrepared is ' + e.duration);
          }
        })
        .onSeeking((e?: TimeObject) => {
          if (e != undefined) {
            console.info('onSeeking is ' + e.time);
          }
        })
        .onSeeked((e?: TimeObject) => {
          if (e != undefined) {
            console.info('onSeeked is ' + e.time);
          }
        })
        .onUpdate((e?: TimeObject) => {
          if (e != undefined) {
            console.info('onUpdate is ' + e.time);
          }
        })
        .onFullscreenChange((e?: FullscreenObject) => {
          if (e != undefined) {
            console.info('onFullscreenChange is ' + e.fullscreen);
          }
        })

      Row() {
        // Replace $rawfile('video2.mp4') and $r('app.media.poster2') with the resource files you use.
        Button('src').onClick(() => {
          this.videoSrc = $rawfile('video2.mp4'); // Switch the video source.
        }).margin(5)
        Button('previewUri').onClick(() => {
          this.previewUri = $r('app.media.poster2'); // Switch the preview image.
        }).margin(5)
        Button('controls').onClick(() => {
          this.showControls = !this.showControls; // Specify whether to show the control bar.
        }).margin(5)
      }

      Row() {
        Button('start').onClick(() => {
          this.controller.start(); // Start playback.
        }).margin(2)
        Button('pause').onClick(() => {
          this.controller.pause(); // Pause playback.
        }).margin(2)
        Button('stop').onClick(() => {
          this.controller.stop(); // Stop playback.
        }).margin(2)
        Button('reset').onClick(() => {
          this.controller.reset(); // Reset the AVPlayer instance.
        }).margin(2)
        Button('setTime').onClick(() => {
          this.controller.setCurrentTime(10, SeekMode.Accurate); // Seek to the 10s position of the video.
        }).margin(2)
      }

      Row() {
        Button('rate 0.75').onClick(() => {
          this.curRate = PlaybackSpeed.Speed_Forward_0_75_X; // Play the video at the 0.75x speed.
        }).margin(5)
        Button('rate 1').onClick(() => {
          this.curRate = PlaybackSpeed.Speed_Forward_1_00_X; // Play the video at the 1x speed.
        }).margin(5)
        Button('rate 2').onClick(() => {
          this.curRate = PlaybackSpeed.Speed_Forward_2_00_X; // Play the video at the 2x speed.
        }).margin(5)
      }
    }
  }
}

interface DurationObject {
  duration: number;
}

interface TimeObject {
  time: number;
}

interface FullscreenObject {
  fullscreen: boolean;
}
```

This example shows how to use the enableAnalyzer attribute to enable AI image analyzer.

```TypeScript
// xxx.ets
@Entry
@Component
struct ImageAnalyzerExample {
  // Replace $rawfile('video1.mp4') and $r('app.media.poster1') with the resource files you use.
  @State videoSrc: Resource = $rawfile('video1.mp4');
  @State previewUri: Resource = $r('app.media.poster1');
  controller: VideoController = new VideoController();
  config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller,
        imageAIOptions: this.options // Set the AI image analysis options.
      })
        .width('100%')
        .height(600)
        .controls(false)
        .enableAnalyzer(true)
        .analyzerConfig(this.config)
        .onStart(() => {
          console.info('onStart');
        })
        .onPause(() => {
          console.info('onPause');
        })

      Row() {
        Button('start').onClick(() => {
          this.controller.start(); // Start playback.
        }).margin(5)
        Button('pause').onClick(() => {
          this.controller.pause(); // Pause playback.
        }).margin(5)
        Button('getTypes').onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes();
        }).margin(5)
      }
    }
  }
}
```

This example demonstrates how to enable the Video component to play a video that is dragged into it.

```TypeScript
// xxx.ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  // Replace $rawfile('video1.mp4') with the image resource file you use.
  @State videoSrc: Resource | string = $rawfile('video1.mp4');
  private controller: VideoController = new VideoController();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .height(600)
        .onPrepared(() => {
          // Execute the controller's start method in the onPrepared callback to ensure the video starts playing immediately after the source is changed.
          this.controller.start();
        })
        .onDrop((e: DragEvent) => {
          // Handle the drop event when a video is dragged into the component.
          // The DragEvent contains the information about the dragged-in video source. After the information is obtained, assign a value to the state variable videoSrc to change the video source of the video.
          let record = e.getData().getRecords()[0];
          if (record.getType() == uniformTypeDescriptor.UniformDataType.VIDEO) {
            let videoInfo = record as unifiedDataChannel.Video;
            this.videoSrc = videoInfo.videoUri;
          }
        })
    }
  }
}
```

This example shows how to set the video fill mode using the objectFit attribute.

```TypeScript
// xxx.ets
@Entry
@Component
struct VideoObject {
  // Replace $rawfile('rabbit.mp4') and $r('app.media.tree') with the resource files you use.
  @State videoSrc: Resource = $rawfile('rabbit.mp4');
  @State previewUri: Resource = $r('app.media.tree');
  @State showControls: boolean = true;
  controller: VideoController = new VideoController();

  build() {
    Column() {
      Text('ImageFit.Contain').fontSize(12)
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width(350)
        .height(230)
        .controls(this.showControls)
        .objectFit(ImageFit.Contain) // Set the video fill mode to ImageFit.Contain.
        .margin(5)

      Text('ImageFit.Fill').fontSize(12)
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width(350)
        .height(230)
        .controls(this.showControls)
        .objectFit(ImageFit.Fill) // Set the video fill mode to ImageFit.Fill.
        .margin(5)

      Text('ImageFit.START').fontSize(12)
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width(350)
        .height(230)
        .controls(this.showControls)
        .objectFit(ImageFit.START) // Set the video fill mode to ImageFit.START.
        .margin(5)
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}
```

This example uses an invalid video resource path to demonstrate how the Video component can obtain error codes through the [onError](#onerror) event, available since API version 20.

```TypeScript
// xxx.ets
@Entry
@Component
struct VideoErrorComponent {
  @State videoSrc: string = "video.mp4"; // Enter an invalid video resource path.
  @State isAutoPlay: boolean = false;
  @State showControls: boolean = true;
  @State showFirstFrame: boolean = false;
  controller: VideoController = new VideoController();
  @State errorMessage: string = '';

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller,
      })
        .width(200)
        .height(120)
        .margin(5)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .onError((err) => {
          // Obtain the error code through the onError event, where code indicates the error code, and message indicates the error message.
          console.error(`code is ${err.code}, message is ${err.message}`);
          this.errorMessage = `code is ${err.code}, message is ${err.message}`;
        })
      // Pass in an invalid video resource path. Expected result: "code is 103602, message is Not a valid source."
      Text(this.errorMessage)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('rgb(213,213,213)')
  }
}
```

The following example demonstrates how to use attributeModifier to dynamically set the attributes and methods of the Video component, including AI image analysis features and playback event methods.

```TypeScript
// xxx.ets
class MyVideoModifier implements AttributeModifier<VideoAttribute> {
  applyNormalAttribute(instance: VideoAttribute): void {
    // Enable the AI image analyzer, which can be triggered by a long press.
    instance.enableAnalyzer(true);
    let config: ImageAnalyzerConfig = {
      types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
    }
    instance.analyzerConfig(config);
    instance.onStart(() => {
      console.info('video: onStart');
    })
    instance.onPause(() => {
      console.info('video: onPause');
    })
    instance.onFinish(() => {
      console.info('video: onFinish');
    })
    instance.onError((err) => {
      console.error('video: onError is code = ' + err.code + ', message = ' + err.message);
    })
    instance.onStop(() => {
      console.info('video: onStop');
    })
    instance.onPrepared((e?: DurationObject) => {
      if (e != undefined) {
        console.info('video: onPrepared is ' + e.duration);
      }
    })
    instance.onSeeking((e?: TimeObject) => {
      if (e != undefined) {
        console.info('video: onSeeking is ' + e.time);
      }
    })
    instance.onSeeked((e?: TimeObject) => {
      if (e != undefined) {
        console.info('video: onSeeked is ' + e.time);
      }
    })
    instance.onUpdate((e?: TimeObject) => {
      if (e != undefined) {
        console.info('video: onUpdate is ' + e.time);
      }
    })
    instance.onFullscreenChange((e?: FullscreenObject) => {
      if (e != undefined) {
        console.info('video: onFullscreenChange is ' + e.fullscreen);
      }
    })
  }
}

@Entry
@Component
struct VideoModifierDemo {
  // Replace $rawfile('video.mp4') with the image resource file you use.
  @State videoSrc: Resource = $rawfile('video.mp4');
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  @State isAutoPlay: boolean = false;
  @State showControls: boolean = false;
  controller: VideoController = new VideoController();
  @State modifier: MyVideoModifier = new MyVideoModifier();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        currentProgressRate: this.curRate, // Set the playback speed.
        controller: this.controller
      })
        .width(300)
        .height(180)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .attributeModifier(this.modifier)
      Row() {
        Button('start').onClick(() => {
          this.controller.start(); // Start playback.
        }).margin(2)
        Button('pause').onClick(() => {
          this.controller.pause(); // Pause playback.
        }).margin(2)
        Button('stop').onClick(() => {
          this.controller.stop(); // Stop playback.
        }).margin(2)
        Button('reset').onClick(() => {
          this.controller.reset(); // Reset the AVPlayer instance.
        }).margin(2)
      }

      Row() {
        Button('Fullscreen').onClick(() => {
          this.controller.requestFullscreen(true); // Enable full-screen mode.
        }).margin(2)
        Button('showControls').onClick(() => {
          this.showControls = !this.showControls; // Specify whether to show the control bar.
        }).margin(2)
      }
    }
  }
}

interface DurationObject {
  duration: number;
}

interface TimeObject {
  time: number;
}

interface FullscreenObject {
  fullscreen: boolean;
}
```
