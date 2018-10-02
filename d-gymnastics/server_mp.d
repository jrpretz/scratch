import std.stdio;
import std.concurrency;

class DataServer_thread{
public:
    double iterate(double d){
        return d*d - 2;
    }
}

class DataServer_interface{
public:
    this(){
        // start a thread
        id_ = spawn(&DataServer_interface.worker,thisTid);
    }

    ~this(){
    }

    void halt(){
        send(id_,Destruct());
        receiveOnly!DestructAck();

    }

    double iterate(double d){
        send(id_,d);
        return receiveOnly!double();
    }


    static void worker(Tid parentId){
        DataServer_thread ds = new DataServer_thread();

        bool canceled = false;
        while(!canceled){
            receive((Destruct d){
                canceled = true;
                send(parentId,DestructAck());
                },
                (double d){
                    send(parentId,ds.iterate(d));
                });
        }
    }

    struct Destruct{}
    struct DestructAck{}

    Tid id_;
}


int main(){

    static if(0){
        auto ds = new DataServer_thread();

        double d1 = 0.34;
        double d2 = 0.34000001;
        for(int i = 0; i < 1000 ; i++){
            writeln(i," ",d1," ",d2);
            d1 = ds.iterate(d1);
            d2 = ds.iterate(d2);
        }
    }

    DataServer_interface dsi = new DataServer_interface();

    double d = 0.56;
    for(int i = 0 ; i < 1000 ; i++){
        writeln(i," ",d);
        d = dsi.iterate(d);
    }

    dsi.halt();

    return 0;
}
