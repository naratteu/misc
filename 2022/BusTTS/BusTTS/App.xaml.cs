using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using Xamarin.Essentials;
using System.Threading.Tasks;
using System.Net.Http;
using System.Collections.Generic;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System.IO;
using System.Text;

namespace BusTTS
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            MainPage = new MainPage();
        }
        protected override async void OnStart()
        {
            using HttpClient client = new HttpClient();
            for (var ts = TimeSpan.FromSeconds(5); ; await Task.Delay(ts))
            {
                var busMsg = bus_msg();
                var timeMsg = DateTime.Now.ToShortTimeString();
                await TextToSpeech.SpeakAsync(timeMsg);
                await TextToSpeech.SpeakAsync(await busMsg);
            }

            async Task<string> bus_msg()
            {
                using var data = new FormUrlEncodedContent(new Dictionary<string, string> { { "arsId", "20571" } });
                using var response = await client.PostAsync("http://m.bus.go.kr/mBus/bus/getStationByUid.bms", data);
                var str = await response.Content.ReadAsStringAsync();
                var j = JObject.Parse(str)["resultList"][0];
                return $"{j["rtNm"]}. {j["arrmsg1"]}";
            }
        }
    }
}
